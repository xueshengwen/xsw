import os.path

holderURLToFilePath = {}
for line in file("index.php"):
    line = line.strip()
    if line.find("if ($url == '") == 0 and line.find("file_get_contents('.") != -1:
        parts = line.split("'")
        assert len(parts) == 5
        holderURLToFilePath[parts[1]] = parts[3]

old = "/web/20160131223221/http://www.apfm.info/"
new = ""

for holderUrl in holderURLToFilePath.keys():
    path = holderURLToFilePath.get(holderUrl, None)
    assert path != None
    path = path.replace("//", "/")


    if os.path.exists(path)  == False:
        # print "Can't find file: ", path, holderUrl
        continue
        # break
    print path

    contents = open(path, 'r').read()
    contents = contents.replace(old, new)

    output = file(path, "w")
    output.write(contents)
    output.close()

    print path
