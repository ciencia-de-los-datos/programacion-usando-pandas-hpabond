"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    num_filas_tbl0 = tbl0.shape[0]
    return num_filas_tbl0


def pregunta_02():
    num_columnas_tbl0 = tbl0.shape[1]
    return num_columnas_tbl0


def pregunta_03():
    conteo_por_letra = tbl0['_c1'].value_counts().sort_index()
    return conteo_por_letra


def pregunta_04():
    promedio_por_letra = tbl0.groupby('_c1')['_c2'].mean()
    return promedio_por_letra



def pregunta_05():
    maximo_por_letra = tbl0.groupby('_c1')['_c2'].max()
    return maximo_por_letra


def pregunta_06():
    df_tbl1 = pd.read_csv("tbl1.tsv", sep='\t')
    valores_unicos = df_tbl1['_c4'].str.upper().unique()
    valores_unicos.sort()
    return valores_unicos.tolist()


def pregunta_07():
    suma_por_letra = tbl0.groupby('_c1')['_c2'].sum()
    return suma_por_letra



def pregunta_08():
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0




def pregunta_09():
 
    tbl0['year'] = tbl0['_c3'].str.split('-').str[0]
    return tbl0[['_c0', '_c1', '_c2', '_c3', 'year']]


def pregunta_10():

    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

    result = tbl0.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()

    result = result.sort_values(by='_c1')

    return result


resultado = pregunta_10()
print(resultado)


def pregunta_11():
    result = tbl1.groupby('_c0')['_c4'].apply(lambda x: ','.join(sorted(x))).reset_index()
    return result



def pregunta_12():

    
    tbl2['_c5'] = tbl2['_c5a'] + ':' + tbl2['_c5b'].astype(str)

    result = tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    
    return result



def pregunta_13():
  
    merged = pd.merge(tbl0, tbl2, left_on='_c0', right_on='_c0')
    result = merged.groupby('_c1')['_c5b'].sum()
    return result
