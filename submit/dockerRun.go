package submit

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/container"
	"github.com/docker/docker/api/types/mount"
	"github.com/docker/docker/client"
	"github.com/docker/docker/pkg/stdcopy"
	"io/ioutil"
	"net/http"
	"time"
)

func IsTokenValid(teamToken string, teamName string) bool {
	url := UserExistUrl + teamToken + "&teamname=" + teamName
	resp, err := http.Get(url)
	if err != nil {
		return false
	}
	defer resp.Body.Close()
	d1, _ := ioutil.ReadAll(resp.Body)
	data := JsonNew.Get(d1)

	if data.Get("data").ToBool() == true {
		return true
	} else {
		return false
	}
}

func RunEncry(tokenpath string, dockerImage string) (int, string, time.Duration, uint64, error) {
	startTime := time.Now()
	memUsageChan := make(chan uint64, 1)

	ctx, cancel := context.WithTimeout(context.Background(), 15*time.Second)
	defer cancel()

	cli, err := client.NewClientWithOpts(client.FromEnv)
	cli.NegotiateAPIVersion(ctx)
	if err != nil {
		return DockerError, "", 0, 0, err
	}

	containerConfig := &container.Config{
		Image: dockerImage,
		//运行run.sh
		Cmd: []string{"/bin/bash", "/app/run.sh"},
	}

	hostConfig := &container.HostConfig{
		AutoRemove:  true,
		CapDrop:     []string{"all"},
		CapAdd:      []string{"SYS_CHROOT"},
		NetworkMode: "none",
		Mounts: []mount.Mount{
			{
				Type:   mount.TypeBind,
				Source: tokenpath,
				Target: "/app",
			},
		},
	}

	resp, err := cli.ContainerCreate(ctx, containerConfig, hostConfig, nil, nil, "")
	if err != nil {
		return DockerError, "", 0, 0, err
	}

	//启动容器
	err = cli.ContainerStart(ctx, resp.ID, types.ContainerStartOptions{})
	if err != nil {
		return DockerError, "", 0, 0, err
	}

	go func() {
		var maxMemUsage uint64 = 0
		defer func() { memUsageChan <- maxMemUsage }()

		for {
			stats, err := cli.ContainerStats(ctx, resp.ID, false)
			if err != nil {
				break
			}
			var containerStats types.StatsJSON
			err = json.NewDecoder(stats.Body).Decode(&containerStats)
			if err != nil {
				break
			}

			memUsage := containerStats.MemoryStats.Usage
			if memUsage > maxMemUsage {
				maxMemUsage = memUsage
			}

			stats.Body.Close()
			time.Sleep(1 * time.Second) // 定时间隔
		}
	}()

	options := types.ContainerLogsOptions{
		Follow:     true,
		ShowStdout: true,
		ShowStderr: true,
		//Timestamps: true,
	}

	//获取日志
	containerLogs, err := cli.ContainerLogs(ctx, resp.ID, options)
	if err != nil {
		return DockerError, "", 0, 0, err
	}
	//等待容器停止
	statusCh, errCh := cli.ContainerWait(ctx, resp.ID, container.WaitConditionNotRunning)
	select {
	case err := <-errCh:
		if err != nil {
			return DockerError, "", 0, 0, err
		}
	case <-statusCh:

	case <-ctx.Done():
		return TimeoutError, "", 0, 0, ctx.Err()
	}

	endTime := time.Now()
	duration := endTime.Sub(startTime)

	var stdout, stderr bytes.Buffer
	_, err = stdcopy.StdCopy(&stdout, &stderr, containerLogs)
	if err != nil {
		return DockerError, "", 0, 0, err
	}
	if stderr.String() != "" {
		return CompileError, stderr.String(), 0, 0, nil
	}

	maxMemUsage := <-memUsageChan

	fmt.Printf("Runtime: %v\n", duration)
	fmt.Printf("Max memory usage: %d bytes\n", maxMemUsage)

	return Success, stdout.String(), duration, maxMemUsage, err

}

func RunDecry(tokenpath string, dockerImage string) (int, string, time.Duration, uint64, error) {
	startTime := time.Now()
	memUsageChan := make(chan uint64, 1)

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	cli, err := client.NewClientWithOpts(client.FromEnv)
	cli.NegotiateAPIVersion(ctx)
	if err != nil {
		return DockerError, "", 0, 0, err
	}

	containerConfig := &container.Config{
		Image: dockerImage,
		Cmd:   []string{"/bin/bash", "/app/run.sh"},
	}

	hostConfig := &container.HostConfig{
		AutoRemove:  true,
		CapDrop:     []string{"all"},
		CapAdd:      []string{"SYS_CHROOT"},
		NetworkMode: "none",
		Mounts: []mount.Mount{
			{
				Type:   mount.TypeBind,
				Source: tokenpath,
				Target: "/app",
			},
		},
	}

	resp, err := cli.ContainerCreate(ctx, containerConfig, hostConfig, nil, nil, "")
	if err != nil {
		return DockerError, "", 0, 0, err
	}

	//启动容器
	err = cli.ContainerStart(ctx, resp.ID, types.ContainerStartOptions{})
	if err != nil {
		return DockerError, "", 0, 0, err
	}

	go func() {
		var maxMemUsage uint64 = 0
		defer func() { memUsageChan <- maxMemUsage }()

		for {
			stats, err := cli.ContainerStats(ctx, resp.ID, false)
			if err != nil {
				break
			}
			var containerStats types.StatsJSON
			err = json.NewDecoder(stats.Body).Decode(&containerStats)
			if err != nil {
				break
			}

			memUsage := containerStats.MemoryStats.Usage
			if memUsage > maxMemUsage {
				maxMemUsage = memUsage
			}

			stats.Body.Close()
			time.Sleep(1 * time.Second) // 定时间隔
		}
	}()

	options := types.ContainerLogsOptions{
		Follow:     true,
		ShowStdout: true,
		ShowStderr: true,
		//Timestamps: true,
	}

	containerLogs, err := cli.ContainerLogs(ctx, resp.ID, options)
	if err != nil {
		return DockerError, "", 0, 0, err
	}
	//等待容器停止
	statusCh, errCh := cli.ContainerWait(ctx, resp.ID, container.WaitConditionNotRunning)
	select {
	case err := <-errCh:
		if err != nil {
			return DockerError, "", 0, 0, err
		}
	case <-statusCh:

	case <-ctx.Done():
		return TimeoutError, "", 0, 0, ctx.Err()
	}

	endTime := time.Now()
	duration := endTime.Sub(startTime)

	var stdout, stderr bytes.Buffer
	_, err = stdcopy.StdCopy(&stdout, &stderr, containerLogs)
	if err != nil {
		return DockerError, "", 0, 0, err
	}
	if stderr.String() != "" {
		return CompileError, stderr.String(), 0, 0, nil
	}

	maxMemUsage := <-memUsageChan

	fmt.Printf("Runtime: %v\n", duration)
	fmt.Printf("Max memory usage: %d bytes\n", maxMemUsage)

	return Success, stdout.String(), duration, maxMemUsage, err

}
