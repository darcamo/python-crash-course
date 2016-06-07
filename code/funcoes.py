

# sample(posicao_final)
def calc_s(t, s0=0, v0=1, a=0.5):
    """Calcula posição final dados s0, v0, a e t."""
    return s0 + v0*t + 0.5 * a * t**2
# end-sample


if __name__ == '__main__':
    fib(6)
