map_of_codons = {
  "AAA" : "Z",
  "ABA" : "T",
  "BCA" : "U",
  "CAA" : "F"
}

mass_of_AA = {
  "Z" : 134.20,
  "T" : 97.52,
  "U" : 174.91,
  "F" : 156.48
}

def TranslateAndWeigh(DNASequence):
  print(f"Received DNA sequence: {DNASequence}")

  translatedSequence = ""
  totalMass = 0

  codon1 = DNASequence[0:3]
  if codon1 in map_of_codons.keys():
    AAToAdd = map_of_codons[codon1]
    translatedSequence += AAToAdd
    totalMass += mass_of_AA[AAToAdd]
  else:
    print("Invalid Sequence")
    return

  codon2 = DNASequence[3:6]
  if codon2 in map_of_codons.keys():
    AAToAdd = map_of_codons[codon2]
    translatedSequence += AAToAdd
    totalMass += mass_of_AA[AAToAdd]
  else:
    print("Invalid Sequence")
    return

  codon3 = DNASequence[6:9]
  if codon3 in map_of_codons.keys():
    AAToAdd = map_of_codons[codon3]
    translatedSequence += AAToAdd
    totalMass += mass_of_AA[AAToAdd]
  else:
    print("Invalid Sequence")
    return

  codon4 = DNASequence[9:12]
  if codon4 in map_of_codons.keys():
    AAToAdd = map_of_codons[codon4]
    translatedSequence += AAToAdd
    totalMass += mass_of_AA[AAToAdd]
  else:
    print("Invalid Sequence")
    return

  print(f"Translated AA sequence: {translatedSequence}")
  print(f"Protein mass: {totalMass}")
