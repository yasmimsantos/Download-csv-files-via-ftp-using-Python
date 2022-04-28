'''
---------------------------------------------------------------------------
|   Connection via FTP and download of 35 .csv files in a local folder    | 
|                           # Python                                      |
|                 Yasmim Senden dos Santos 08/11/2021                     | 
---------------------------------------------------------------------------

'''

from ftplib import FTP_TLS
ftps = FTP_TLS('EnterFtpAddressHere')
ftps.login('EnterYourLogin', 'TypeYourPassword')           
ftps.prot_p()          # switch to secure data connection.. IMPORTANT! Otherwise, only the user and password is encrypted and not all the file data.
ftps.retrlines('LIST')

filename = 'ATEG_REGIONAL_MG_DADOS_TB_ATIVIDADE.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_CATEGORIA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_COLUNA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_CULTURA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_CULTURA_VARIEDADE.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_GRUPO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_HIS_PROPRIEDADE_AREA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_HIS_TALHAO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_IR.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_IR_COLUNA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_IR_OBSERVACAO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_ITEM.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_MUNICIPIO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROJETO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE_AREA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE_ATIVIDADE.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE_CULTURA_SECUNDARIA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE_PROJETO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE_TECNICO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_PROPRIEDADE_USUARIO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_RATEIO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_RATEIO_ITEM.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_RATEIO_ITEM_OBSERVACAO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_SAFRA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_SITUACAO_VISITA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_SUBGRUPO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_TALHAO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_TALHAO_CULTURA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_TIPO_COLUNA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_UNIDADE_MEDIDA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_USUARIO.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_USUARIO_CATEGORIA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_VISITA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

filename = 'ATEG_REGIONAL_MG_DADOS_TB_VISITA_COLUNA.csv'
print ('Download of the file ' + filename)
myfile = open(filename, 'wb')

ftps.retrbinary('RETR %s' % filename, myfile.write)

print('Download of CSV files completed successfully.')

ftps.close()



