
#include <stdio.h>
#include <jpeglib.h>
#include <assert.h>
#include <string.h>

#define B_H(byte) ((((unsigned char)byte & 0x80)>>7)&0x1)
#define B_L(byte) (byte & 0x1)
int main(int argc, char** argv)
{
    const char* INFILE = argv[1];
    const char* OUTFILE = argv[2];
    const char* key = argv[3];
      struct jpeg_compress_struct cinfo;
      struct jpeg_decompress_struct dinfo;
    struct jpeg_error_mgr jerr;
      cinfo.err = jpeg_std_error(&jerr);
    dinfo.err = jpeg_std_error(&jerr);
      jpeg_create_compress(&cinfo);	
    jpeg_create_decompress(&dinfo);
    
    FILE *infile,*outfile;
    outfile=fopen(OUTFILE,"wb");
    infile=fopen(INFILE,"rb");
    assert(infile!=NULL);
    assert(outfile!=NULL);
    jpeg_stdio_src(&dinfo, infile);
    jpeg_stdio_dest(&cinfo, outfile);

    jpeg_read_header(&dinfo,TRUE);
    
    cinfo.dct_method=JDCT_ISLOW;

    jvirt_barray_ptr* coeff= jpeg_read_coefficients(&dinfo);
    char str[20];//"xhdzero";
    strcpy(str, key);
    size_t b_lenstr=strlen(str);
    unsigned char wcurbyte=(unsigned char)str[0];//jsteg f3 f5
    size_t wcuri=0,wcurii=0;
    int ever_accessed;
    for (int ci = 0; ci < 1; ci++)
        {
        if(wcuri>=b_lenstr)break;
        JBLOCKARRAY buffer_one;
        JCOEFPTR blockptr_one;
        jpeg_component_info* compptr_one;
        compptr_one = dinfo.comp_info + ci;

        for (int by = 0; by < compptr_one->height_in_blocks; by++)
        {
            buffer_one = (dinfo.mem->access_virt_barray)((j_common_ptr)&dinfo, coeff[ci], by, (JDIMENSION)1, TRUE);
            for (int bx = 0; bx < compptr_one->width_in_blocks; bx++)
            {
                blockptr_one = buffer_one[0][bx];
                for (int bi = 0; bi < 64; bi++)
                {
                    ever_accessed=0;
                    if(blockptr_one[bi]!=0 )
                    {
                        if(B_L(blockptr_one[bi])!=(char)B_H(wcurbyte) && (blockptr_one[bi]==1 || blockptr_one[bi]==-1) )
                        {
                            blockptr_one[bi]=0;//invalidate
                        }else	if(B_L(blockptr_one[bi])!=(char)B_H(wcurbyte))
                        {
                            if(blockptr_one[bi]>0)blockptr_one[bi]--;
                            else					blockptr_one[bi]++;
                            ever_accessed=1;
                        }else{
                            ever_accessed=1;
                            //do not change but it's still valid
                        }
                    }

                    if(ever_accessed)
                    {
                        wcurii++;
                        if(wcurii==8)
                        {
                            wcurii=0;
                            wcuri += 1;
                            if(wcuri >= b_lenstr)goto end_embed;
                            wcurbyte =(unsigned char)str[wcuri];
                            printf(" ");
                        }else{
                            wcurbyte = (wcurbyte << 1);
                        }
                    }
                }
              }
            }
        }

    end_embed:
    jpeg_copy_critical_parameters(&dinfo,&cinfo);
      cinfo.input_components = 3;
      cinfo.in_color_space = JCS_RGB;
    jpeg_write_coefficients(&cinfo,coeff);
    
    jpeg_finish_compress(&cinfo);
    jpeg_finish_decompress(&dinfo);

    fclose(infile);
    fclose(outfile);
    jpeg_destroy_decompress(&dinfo);
    jpeg_destroy_compress(&cinfo);
}
