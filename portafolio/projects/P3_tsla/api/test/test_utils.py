from P3_tsla.api.utils import getWindowFromDate

window = getWindowFromDate(
    "2016-01-06"
)

print("=" * 50)
print("COLUMNAS")
print(window.columns)

print("=" * 50)
print("HEAD")
print(window.head())

print("=" * 50)
print("SHAPE")
print(window.shape)