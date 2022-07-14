def likes(num_likes):
  if num_likes >= 1000000:
    return str(num_likes // 1000000) + 'MILLION'
  elif num_likes >= 1000:
    return str(num_likes // 1000) + 'K'

  return num_likes

if __name__ == '__main__':
  print(likes(999))
  print(likes(1000000))
  print(likes(1500))