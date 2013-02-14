import os, zipfile, time, utils

def zip(src, dst):
	zipname = time.strftime("%Y%m%d-%H%M%S") + ".zip"
	ignore = utils.ignore(dst,src)
	paths = []
	if os.path.exists(dst): #zipping dstination files
		zip = zipfile.ZipFile(zipname, "w")
		for root, dirs, files in os.walk(dst):
			if root not in ignore:
				for file in files:
					if os.path.join(dst,file) not in ignore:
						zip.write(os.path.join(root, file))

		zip.close()

if __name__ == "__main__":
	args = utils.config()
	copy(args['src'],args['dst'])