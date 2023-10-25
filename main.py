# Input
from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.dnaconvert import *

def argparserLocal():
    from argparse import ArgumentParser
    ''' Argument parser for the commands '''
    parser = ArgumentParser(prog='myseq',description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:', 
        dest='command')
    subparsers.required = True
    
    cgc_command = subparsers.add_parser('gcContent',help='Calculate GC content')
    cgc_command.add_argument("-s","--seq",type=str,default=None,help="provide sequence")

    count_command = subparsers.add_parser('countBases',help='Count number of each base')
    count_command.add_argument("-s","--seq",type=str,default=None,help="provide sequence")
    count_command.add_argument("-r","--revcomp",type=str,default=None,help="Convert DNA to reverse-complementary")

    transcription_command = subparsers.add_parser('transcription',help='Convert DNA->RNA')
    transcription_command.add_argument("-s","--seq",type=str,default=None,help="provide sequence")
    transcription_command.add_argument("-r","--revcomp",type=str,default=None,help="Convert DNA to reverse-complementary")

    translation_command = subparsers.add_parser('translation',help='Convert DNA->Protein')
    translation_command.add_argument("-s","--seq",type=str,default=None,help="provide sequence")
    translation_command.add_argument("-r","--revcomp",type=str,default=None,help="Convert DNA to reverse-complementary")

    enz_command = subparsers.add_parser('enzTargetsScan',help='Find restriction enzyme')
    enz_command.add_argument("-s","--seq",type=str,default=None,help="provide sequence")
    enz_command.add_argument("-e","--enz",type=str,default=None,help="Enzyme name")
    enz_command.add_argument("-r","--revcomp",type=str,default=None,help="Convert DNA to reverse-complementary")

    return parser
# def test(): 
#     parser = argparserLocal()
#     args = parser.parse_args(["transcription","-s","ATGGGccGTAGAATTCTTGCaaGCCCGT"])
#     print("Input",args.seq,"\ntranscription = ", dna2rna(args.seq))

def main():
    parser = argparserLocal()
    args = parser.parse_args()
    # print(args.seq)

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
        # print(seq)
    
    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq))

    if args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        print("Input",args.seq,"\ntranscription =", dna2rna(seq))

    if args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        print("Input",args.seq,"\ntranslation =", dna2protein(seq))  

    if args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        print("Input",args.seq,"\ncountBases =", countBasesDict(seq))
    
    




    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    # seq = seq.upper()
    # print("Transcription: ", dna2rna(seq))
    # print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    # print("Translation: ", dna2protein(seq))
    # print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    # print("GC Content:", gcContent(seq))
    # print("Count Bases: ", countBasesDict(seq))
    # print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    # print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    # print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

if __name__ == "__main__":
    main()
    #test()