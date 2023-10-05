def chambai():
  INP_name = 'AI BTX'
  
  from s01_dapan import hi
  r_DAPAN = hi()  # aka result_of_DAPAN

  try:
    from s00_bailam import hi
    r_THISINH = hi()  # aka result_of_THISINH
  except:
    r_THISINH = None

  chambai_r = int(r_THISINH == r_DAPAN)
  return chambai_r
