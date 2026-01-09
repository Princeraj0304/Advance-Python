marks={'Mike':90,'Remy':92,'Sally':34,'Ellie':45}

# def markss(stu):
#     return marks[stu]>=90   


# x=filter(markss,marks)

x=filter(lambda mark: marks[mark]>=90,marks)

for i in x:
    print(i)


# for i in marks:
#     print(marks)