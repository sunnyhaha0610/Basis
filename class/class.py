class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrc:
            print ("Not Supported")
        else:
            print("Read from",src)
        print(IO.supportedSrcs)
        IO.read("file")
        IO.read("internet")