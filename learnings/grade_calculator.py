# | Marks    | Grade |
# | -------- | ----- |
# | 90–100   | A     |
# | 75–89    | B     |
# | 60–74    | C     |
# | Below 60 | Fail  |

marks = int(input('Enter your marks : '))

if marks >= 90:
	print('Grade: A')
elif marks >= 75:
	print('Grade: B')
elif marks >= 60:
	print('Grade: C')
else:
	print('Grade: Fail')