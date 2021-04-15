def leaderbordSave(name='unnamed', time='100 years'):
    line=str(name+'/'+time)
    file = open("leaderboard.txt","a")
    file.write(line+'\n')
