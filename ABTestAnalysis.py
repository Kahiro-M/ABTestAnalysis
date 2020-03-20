#!/usr/bin/python
# coding: UTF-8
# -*- Coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy import stats

html_header = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style type="text/css">
      <!--
      table {
        display:inline;
        border:1px lightgray;
        margin-right: 3px;
        }
      -->
    </style>
  </head>
  <body>
"""

html_footer = """
  </body>
</html>
"""

a_csvData = pd.read_csv("./A.csv",encoding="utf_8")
b_csvData = pd.read_csv("./B.csv",encoding="utf_8")

anlyDf = pd.DataFrame({
  "User":np.concatenate([a_csvData.A_user,b_csvData.B_user]),
  "Group":np.concatenate([np.tile("A",len(a_csvData.A_data)),(np.tile("B",len(b_csvData.B_data)))]),
  "Data":np.concatenate([a_csvData.A_data,b_csvData.B_data]),
})
abDf=pd.crosstab(
  index=anlyDf["Group"],
  columns=anlyDf["Data"]
)

chi2Value, chi2PValue, chi2DoF, chi2EF = stats.chi2_contingency(abDf, correction=False)
chi2ResultStrPVal = "p値 : "+str('{:.10f}'.format(chi2PValue))
chi2ResultStrVal = "カイ二乗値 : "+str(chi2Value)
chi2ResultStrDoF = "自由度 : "+str(chi2DoF)
if chi2PValue<0.05:
  resultStrChi2Test = "<b>カイ二乗検定　<font color=red>有意差あり(GroupとDataには関連がある)</font></b>"
else:
  resultStrChi2Test = "<b>カイ二乗検定　有意差なし(GroupとDataには関連がない)</b>"

np.array([[2,2],[2,2]]).shape
if np.array([[2,2],[2,2]]).shape != abDf.shape:
  fisherResultStrPVal = "２要素 x ２群の計４パターンで表現できる入力データで実行してください。"
  resultStrFisherTest = "<b>要素が多すぎるため、フィッシャーの正確検定を実行できませんでした。</b>"
else:
  fisherOddsRatio, fisherPValue = stats.fisher_exact(abDf)
  fisherResultStrPVal = "p値 : "+str('{:.10f}'.format(fisherPValue))
  if fisherPValue<0.05:
    resultStrFisherTest = "<b>フィッシャーの正確検定　<font color=red>有意差あり(GroupとDataには関連がある)</font></b>"
  else:
    resultStrFisherTest = "<b>フィッシャーの正確検定　有意差なし(GroupとDataには関連がない)</b>"


abDf4display=pd.crosstab(
  index=anlyDf["Group"],
  columns=anlyDf["Data"],
  margins=True, 
  normalize=False
)

# html output
with open("result.html", mode="w", encoding="utf_8") as fileObj:
  fileObj.write(html_header)
  fileObj.write(resultStrChi2Test)
  fileObj.write("<br>")
  fileObj.write(chi2ResultStrPVal)
  fileObj.write("　　")
  fileObj.write(chi2ResultStrVal)
  fileObj.write("　　")
  fileObj.write(chi2ResultStrDoF)
  fileObj.write("<br>")
  fileObj.write("<br>")
  fileObj.write(resultStrFisherTest)
  fileObj.write("<br>")
  fileObj.write(fisherResultStrPVal)
  fileObj.write("<br>")
  fileObj.write("<br>")
  fileObj.write("<br>")
  fileObj.write("入力データ")
  fileObj.write(anlyDf.to_html())
  fileObj.write("　　　クロス集計表")
  fileObj.write(abDf4display.to_html())
  fileObj.write("<br>")
  fileObj.write(html_footer)
