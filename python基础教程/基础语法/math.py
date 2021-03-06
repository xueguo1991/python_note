#-----------------------------------
# python 内置数学运算
#-----------------------------------

# 加法
plus_int = 12 + 5
plus_float = 12.2474545 + 5.98321213232
print(plus_int, plus_float)

# 减法
minus_int = 100 - 80
minus_float = 13.778822223212 - 2.7788445212
print(minus_int, minus_float)

# 乘法
multiply_int = 12 * 50
multiply_float = 12.7734337 * 4.5531244455
print(multiply_int, multiply_float)

# 除法
division_int = 5 / 3
division_float = 4.5573 / 3.5677
print(division_int, division_float)

# 取余 取模
modulo_int = 23 % 10
modulo_float = 15.33 % 12
print(modulo_int, modulo_float)

# 幂
power_int = 23 ** 2
power_float = 15.5 ** 2.3
print(power_int, power_float)

# 除法取整
truncate_int = 12 // 5
truncate_float = 144.333  // 33
print(truncate_int, truncate_float)

# 表示16进制数
var_dec = 1001
var_hex = 0x3e9
print('数值 {:d} 的十六进制表示为 {:s}'.format(var_hex,hex(var_dec)))

# 表示8进制数
var_oct = 0o1751
print('数值 {:d} 的八进制表示为 {:s}'.format(var_oct,oct(var_dec)))

# 表示二进制数
var_bin = 0b1111101001
print('数值 {:d} 的二进制表示为 {:s}'.format(var_bin,bin(var_dec)))
