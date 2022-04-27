class StringUtility:
  def __init__(self, string):
    self.string = string;
    
  def __str__(self):
    return self.string
    
  def vowels(self):
    sWithVowels = "aeiouAEIOU"
    count = 0
    for eachChar in self.string:
      if eachChar in sWithVowels:
        count += 1
    if count >= 5:
      return "many"
    else:
      return str(count)
      
  def bothEnds(self):
    if(len(self.string) <= 2):
      return ''
    return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]

  def fixStart(self):
    if(len(self.string) <= 1):
      return self.string
    firstchar = self.string[0]
    NewString = self.string[0]
    for i in range(1,len(self.string)):
        if self.string[i] == firstchar:
          NewString = NewString + '*'
        else:
          NewString = NewString + self.string[i]
    return NewString
    
  def asciiSum(self):
    count = 0
    for eachChar in self.string:
      asciiCharValue = ord(eachChar)
      count += asciiCharValue
    return count

  def cipher(self):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = uppercase.lower()
    shiftamount = len(self.string)
    returnstring = ''
    for char in self.string:
      if char in uppercase:
        indexupper = uppercase.find(char)
        resultingupperindex = indexupper+shiftamount
        while resultingupperindex >= 26:
          resultingupperindex -= 26
        returnstring = returnstring + uppercase[resultingupperindex]
      elif char in lowercase:
        indexlower = lowercase.find(char)
        resultinglowerindex = indexlower+shiftamount
        while resultinglowerindex >= 26:
          resultinglowerindex -= 26
        returnstring = returnstring + lowercase[resultinglowerindex]
      else:
          returnstring = returnstring + char
    return returnstring

        
  