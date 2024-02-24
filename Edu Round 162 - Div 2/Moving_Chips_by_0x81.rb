def ga = gets.split.map!(&:to_i)
def gi = gets.to_i
def giga = [gi, ga]
def gigs = [gi, gs]
def gs = gets.strip
def gss = gs.split
def o(x) = puts(x)
def pa(a, d = ' ') = puts(a * d)
def pan(a) = pa(a, "\n")
def yn(p) = p ? 'YES' : 'NO'
def ync(p) = p ? 'Yes' : 'No'
def ynd(p) = p ? 'yes' : 'no'
def hz(d = 0) = Hash.new(d)
def rqr(*a) = a.each { require _1 }

class Set def z = size end
class Array
    def r = reverse
    def r! = reverse!
    def f = first
    def l = last
    def sh = shift
    def j(...) = join(...)
    def pc = pack('c*')
    def psum!(s = 0) = map! { s += _1 }
    def lbound(x) = bsearch { _1 >= x }
    def lbound_index(x) = bsearch_index { _1 >= x }
    def hoare!(...) = shuffle!.sort!(...)
    def hoare_by!(...) = shuffle!.sort_by!(...)
    def z = size
end
module Enumerable
    def e(...) = each(...)
    def ei(...) = each_index(...)
    def re(...) = reverse_each(...)
    def ec(...) = each_cons(...)
    def es(...) = each_slice(...)
    def wo(...) = with_object(...)
    def wi(...) = with_index(...)
    def ewi(...) = each_with_index(...)
    def ewo(...) = each_with_object(...)
    def fold(...) = reduce(...)
end
class String
    def i(...) = to_i(...)
    def f = to_f
    def e(...) = each_char(...)
    def eb(...) = each_byte(...)
    def b = bytes
    def r = reverse
    def z = size
end
class Numeric
    def f = to_f
    def i = to_i
    def s(...) = to_s(...)
    def sqrt = Math.sqrt(self)
    def isqrt = Integer.sqrt(self)
end
class Integer
    def p = pred
    def n = succ
    def t(...) = times(...)
    def popcount = loop.reduce((raise if (x = self) < 0; 0)) \
        { | r | break r if x < 1; r += x & 1; x >>= 1; r }
    def ctz = loop.reduce((raise if (x = self) <= 0; 0)) \
        { | r | break r if x[0] == 1; x >>= 1; r.n }
end
class Hash
    def ek(...) = each_key(...)
    def ev(...) = each_value(...)
    def kmin = ek.min
    def kmax = ek.max
    def vmin = ev.min
    def vmax = ev.max
    def d(...) = delete(...)
    def z = size
end
    class MSet < Hash
        def <<(x) = (self[x] = (self[x] || 0).n; self)
        def d(x) = (self.delete x if (self[x] && self[x] -= 1) == 0)
        def each(...) = ek(...)
        def ===(x) = has_key?(x)
    end
    class PQ
        def initialize array = [], heapify = true, &is_unordered
            raise ArgumentError.new 'PQ init' unless
                array.class == Array &&
                (heapify == true || heapify == false) &&
                block_given?
            @a, @u = array, is_unordered
            return unless heapify
            i = @a.size / 2
            sink i while (i -= 1) >= 0
        end
        def size = @a.size
        def empty? = @a.empty?
        def top = @a.first
        def push_pop(x) = !@a.empty? && @u.(x, @a.first) ? pop_push(x) : x
        def pop_push x
            t, @a[0], = @a.first, x
            sink 0
            t
        end
        def << x
            i = @a.size
            @a << x
            while i > 0
                p = (i - 1) / 2
                break unless @u.call @a[p], @a[i]
                @a[p], @a[i] = @a[i], @a[p]
                i = p
            end
            self
        end
        def pop
            return @a.pop if @a.size < 2
            t, @a[0] = @a.first, @a.pop
            sink 0
            t
        end
        private
        def sink p
            z = @a.size
            while (c = p * 2 + 1) < z
                r = c + 1
                c = r if r < z && @u.(@a[c], @a[r])
                break unless @u.call @a[p], @a[c]
                @a[p], @a[c] = @a[c], @a[p]
                p = c
            end
        end
    end
    class MinQ < PQ
        def initialize(a = [], h = true) = super(a, h) { _1 > _2 }
    end
    class MaxQ < PQ
        def initialize(a = [], h = true) = super(a, h) { _1 < _2 }
    end
    def fio(a = 'input.txt', b = 'output.txt')
        $stdin = File.open a, 'rb'
        $stdout = File.open b, 'wb'
    end
    rqr 'set', 'prime'
    class Set def d(...) = delete(...) end
    class Prime
        def self.at_least(x) =
            loop { Prime.prime?(x) ? (break x) : x += 1 }
    end
    def sync = ($stdout.sync = true)
    M007 = 1_000_000_007
    M353 = 998_244_353
    RC = /(.)\1*/
    
    ################################################################
    #                                                              #
    #              https://github.com/alantudyk/Stop               #
    #                                                              #
    ################################################################
    
    gi.t do
        a = giga.l
        o a.rindex(1).n - a.index(1) - a.count(1)
    end
    
    ################################################################
    #                                                              #
    #              https://github.com/alantudyk/Stop               #
    #                                                              #
    ################################################################
    
    