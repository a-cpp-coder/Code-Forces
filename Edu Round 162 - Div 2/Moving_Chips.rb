# class Integrer
#     def n = succ
# end

gets.to_i.times do
    n = gets.to_i
    arr = gets.split.map &:to_i
    first = arr.index(1)
    last = arr.rindex(1)
    # p last
    arr_2 = arr[first..last]
    # p arr_2
    puts arr_2.count(0)
end