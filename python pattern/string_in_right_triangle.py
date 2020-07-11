def tr(text):
    for line in range(1,len(text)+1):
        for col in range(0,line):
            print(text[col],end=" ")
        print()
tr("Python")
tr("manash")
