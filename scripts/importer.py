import dendropy\
import sys

amphib = dendropy.DnaCharacterMatrix.get(
    path=sys.argv[0],
    schema=sys.arv[1]
)

amphib.write_to_path(sys.argv[2], schema=sys.argv[3])