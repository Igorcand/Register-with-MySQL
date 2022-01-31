from PyQt5 import uic, QtWidgets
import mysql.connector as mysql
banco = mysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='CADASTRO'
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria=''
    if formulario.radioButton.isChecked():
        print("Categoria Eletronicos selecionada")
        categoria = 'Eletrônicos'

    elif formulario.radioButton_2.isChecked():
        print("Categoria Informatica selecionada")
        categoria = 'Informática'

    elif formulario.radioButton_3.isChecked():
        print("Categoria Informatica selecionada")
        categoria = 'Alimentos'

    else:
        print("Nenhuma catagoria selecionada")

        categoria = 'Sem Categoria'



    print("Código:", linha1)
    print("Descricao:", linha2)
    print("Preco", linha3)


    cursor = banco.cursor()
    comando_SQL = 'insert into produtos (codigo, descrição, preço, categoria) values(%s, %s, %s, %s)'
    dados = (str(linha1), str(linha2), str(linha3), str(categoria))
    cursor.execute(comando_SQL, dados)
    banco.commit()


#cursor.execute('CREATE TABLE TB_ELETRONICOS(codigo INT(10), descrição VARCHAR(255), preço DEC(10, 2))')
app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

