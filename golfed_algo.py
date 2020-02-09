from job_queue import JobQueue;from functions import prop as p,set_prop as s_p,every as e,reduce as r,foreach as fe,is_zero as i_z,getter as gr,getter_setter as gr_sr
def round_robin(data, Q):
    PID,AT,BT,RM,CMP,TT,WT,c_tt,c_wt,s_tt,s_wt,i_c,s_c,p_d,g_c=gr('PID'),gr('AT'),gr('BT'),gr_sr('RM'),gr_sr('CMP'),gr_sr('TT'),gr_sr('WT'),lambda j:CMP(j)-AT(j),lambda j:TT(j)-BT(j),lambda j:TT(j,c_tt(j)),lambda j:WT(j,c_wt(j)),lambda j:i_z(RM(j)),lambda s:e(lambda j:i_c(j),s),lambda d:list(map(lambda j:RM(j,BT(j)),d)),lambda q,g:lambda t:g.append({'time':t,'queue':list(map(lambda a:PID(a),q.to_array()))});s,t,q,g=p_d(data[:]),0,JobQueue(),[];q_t, r_t = t + Q, g_c(q, g)
    while not s_c(s):
        for j in s:
            if AT(j)==t:q.enqueue(j);r_t(t)
        if t < q_t:
            if i_c(q.peek()):j,q_t=q.dequeue(),t+Q;CMP(j, t);r_t(t);
            q.decrease_rem_time()
        elif t==q_t:j= q.dequeue();q.enqueue(j) if not i_c(j) else CMP(j,t);q.decrease_rem_time();q_t+=Q;r_t(t)
        t += 1
    CMP(q.dequeue(),t);r_t(t);fe(s_tt, s);fe(s_wt, s);t_tt,t_wt=r(lambda j,a:TT(j)+a,s,0),r(lambda j,a:WT(j)+a,s,0);a_tt,a_wt=round(t_tt/len(s),2),round(t_wt/len(s),2);return{'gantt':g,'total_time':t,'avg_tt':a_tt,'avg_wt':a_wt,'sched':s}
