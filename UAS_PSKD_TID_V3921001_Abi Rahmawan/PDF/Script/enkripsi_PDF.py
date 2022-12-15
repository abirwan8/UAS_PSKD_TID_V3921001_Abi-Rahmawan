from PyPDF2 import PdfFileWriter, PdfFileReader
  
# buat objek pdf writer
out = PdfFileWriter()
  
# buka file pdf asli 
file = PdfFileReader("D:/SKD/file_pdf.pdf")
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for idx in range(num):
    
   
    page = file.getPage(idx)
      

    out.addPage(page)
  
  
# masukkan password enkripsi 
password = "abirahmawan_skd"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("D:/SKD/file_pdf_terenkripsi.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)
