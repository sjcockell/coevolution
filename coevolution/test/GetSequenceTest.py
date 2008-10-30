
import coevolution.GetSequence as sh

seqhandler = sh.GetSequence('55980150')
id = seqhandler.get_sequence_id()
print id
seq = seqhandler.get_sequence()
print seq
seqhandler.write_sequence_file()
