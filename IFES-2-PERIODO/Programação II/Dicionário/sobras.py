
def main():
    d = { 0: '', 'I': '1', 'II':'2', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
         11: 'XI', 12: 'XII', 13: 'XIII', 14:'XIV', 15: 'XV', 16:'XVI', 17:'XVII', 18:'XVIII', 19:'XIX', 20: 'XX', 30: 'XXX',
         40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 
         700: 'DCC', 800: 'DCCC', 900: 'CM' }
    
    # Invertendo as chaves e valores e ordenando as chaves alfabeticamente
    d_inverse = {value: key for key, value in d.items()}
    d_sorted = {k: d_inverse[k] for k in sorted(d_inverse)}
    
    print(d_sorted)

main()