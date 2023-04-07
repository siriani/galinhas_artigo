import matplotlib.pyplot as plt
import numpy
from sklearn import metrics


predito = open("predito.txt", "r")
actual1 = open("real.txt", "r")
predicted = []
actual = []
for linha in predito:

    linha = linha[0:5].split(",")
    for valores in linha:
        predicted.append(int(valores))
print(predicted)
for linha in actual1:
    linha = linha[0:5].split(",")
    for valores in linha:
        actual.append(int(valores))

confusion_matrix = metrics.confusion_matrix(actual, predicted, labels=[0,1, 2, 3, 4, 5, 6])


cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0,1, 2, 3, 4, 5, 6])

cm_display.plot()
plt.show()