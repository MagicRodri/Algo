import os
import zipfile
from shutil import copyfile, rmtree

import openpyxl
import PIL
import xlrd
import xlwt


def save_xlsm(wb, xlsmname):
    '''Some crazy workaround to fix what openpyxl cannot when recreating an xlsm file. 
    '''

    # Unzip original and tmp into separate dirs
    PAD = os.getcwd()
    wb.save('tmp.xlsx')
    with zipfile.ZipFile(xlsmname, 'r') as z:
        z.extractall('./xlsm/')
    with zipfile.ZipFile('tmp.xlsx', 'r') as z:
        z.extractall('./xlsx/')
    # copy pertinent left out macro parts into tmp
    copyfile('./xlsm/[Content_Types].xml', './xlsx/[Content_Types].xml')
    copyfile('./xlsm/xl/_rels/workbook.xml.rels',
             './xlsx/xl/_rels/workbook.xml.rels')
    copyfile('./xlsm/xl/vbaProject.bin', './xlsx/xl/vbaProject.bin')
    copyfile('./xlsm/xl/sharedStrings.xml', './xlsx/xl/sharedStrings.xml')
    # create a new tmp zip to rebuild the xlsm
    z = zipfile.ZipFile('tmp.zip', 'w', zipfile.ZIP_DEFLATED)
    # put all the parts back into the new Frankenstein
    os.chdir('./xlsx')
    for root, dirs, files in os.walk('./'):
        for file in files:
            z.write(os.path.join(root, file))
    z.close()
    os.chdir(PAD)
    # humanize Frankenstein
    bakname = xlsmname + '.bak'
    if os.access(bakname, os.W_OK):
        os.remove(bakname)
    os.rename(xlsmname, bakname)
    os.rename('tmp.zip', xlsmname)
    #clean
    rmtree('./xlsm/')
    rmtree('./xlsx/')
    os.remove('./tmp.xlsx')


def main():
    # PIL.WmfImagePlugin.register_handler()
    wb = openpyxl.load_workbook('template.xlsm', keep_vba=True)
    sheet = wb.worksheets[1]
    sheet['E6'] = '=M6-J6'
    print(sheet['A1'].value)
    print(sheet['B1'].value)
    wb.save('test.xlsm')


if __name__ == '__main__':
    main()