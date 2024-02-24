gets.to_i.times do
    n, k = gets.split.map &:to_i
    a = gets.split.map &:to_i
    x = gets.split.map &:to_i
    
    list = a.zip(x)
    # list = list.sort_by{|key, value| value.abs}
    list = list.sort_by{|key, value| -value.abs}
    result = "YES"
    list.each_index(|i| list[i][0] += 1)
    # while list.length > 0
    #     curr_shot = k
    #     while curr_shot > list[n-1][0]:
    #         curr_shot -= list[n-1][0]
    #         n -= 1 
    #         list.pop
    #     end
    #     list[n-1][0] -= curr_shot
    #     list.map{|i| list[i][1]  }
    # end
    puts list
end