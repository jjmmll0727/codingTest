word_dict = {
  'word' : ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'plus', 'minus'],
  'number' : [0,1,2,3,4,5,6,7,8,9,'+','-']
}

def StringChallenge(strParam):
  ''' 
  1. change word to number with blank
  '''
  ans = strParam
  for i in range(len(word_dict['word'])):
    if word_dict['word'][i] in strParam:
      if word_dict['word'][i] == 'minus' or word_dict['word'][i] == 'plus':
        ans = ans.replace(word_dict['word'][i], ' '+str(word_dict['number'][i])+' ')
      ans = ans.replace(word_dict['word'][i], str(word_dict['number'][i]))

  '''
  2. split expression and evaluate
  '''

  ans = ans.split(' ')
  resultList = list() ## list for accumulated result
  resultList.append(int(ans[0]))
  for i in range(len(ans)):
    if ans[i] == '+':
      a = int(resultList[-1])
      b = int(ans[i+1])
      resultList.append(a+b)
    elif ans[i] == '-':
      a = int(resultList[-1])
      b = int(ans[i+1])
      resultList.append(a-b)
  

  '''
  3. change number to word again
  '''

  resultWord = '' ## final answer
  resultNum = str(resultList[-1]) ## final evaluation result ex)18 or -10
  for i in range(len(resultNum)):
    if resultNum[i] == '-':
      resultWord += 'negative'
    else:
      resultWord += word_dict['word'][int(resultNum[i])]
  return resultWord

# keep this function call here 
print(StringChallenge(input()))




'''
=================================================================
'''

