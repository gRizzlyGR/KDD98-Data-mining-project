__author__ = 'Giuseppe'

import os

path = "./images/expl_rep/"
directory = "."
extension = ".png"
files = [file for file in os.listdir(directory) if file.lower().endswith(extension)]

##for file in files:
##   print r"\begin{figure}[!ht]"
##   print r"\centering"
##   print r"\includegraphics{%s%s}" % (path, file[:-4])
##   #print r"\caption{File %s}" % file
##   print r"\end{figure}"

tex = open("expl_rep.tex", "w")

for file in files:
   tex.write("\\begin{figure}\n")
   #tex.write("\centering\n")
   tex.write("\includegraphics{%s%s}\n" % (path, file[:-4]))
   #print r"\caption{File %s}" % file
   tex.write("\end{figure}\n")

tex.close()
