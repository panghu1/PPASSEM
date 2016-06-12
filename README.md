# Run PPASSEM

1. Use KmerCount.py to generate binary input file or use JELLYFISH
  first argument is reads file name
  second argument is kmer length
  third argument is output file name

  Example: python KmerCount.py test_case.fq 23 input.bin

2. Use binary file as input for executing PPASSEM (e.g. input.bin)
  first argument is number of process(NP)
  second argument is header length
  third argument is kmer length
  fourth argument is input file name(with path)
  fifth argument is communication mode (OPTIONAL), 0 for NonBlocking, 1 for Blocking

  Example: mpirun -np NP ./ppassem-1.0-Linux-x64-sparseharsh-boost 3 23 /PATH/TO/FILE/input.bin 

