for kk in range(100):
    k = np.random.choice( np.arange(4*train.shape[0]//5,train.shape[0]))
    if train.loc[k,'sentiment']=='neutral': continue #boring
    if len(train.loc[k,'text'])>95: continue #too wide for display
    
    # EXTRACT INFLUENCIAL TEXT
    last_conv_output,_, pred_vec = cam_model.predict([ids[k:k+1,:],att[k:k+1,:],tok[k:k+1,:]])
    last_conv_output = np.squeeze(last_conv_output)
    pred = np.argmax(pred_vec)
    layer_weights = all_layer_weights[:, pred]
    final_output = np.dot(last_conv_output, layer_weights)
    if pr[pred]!=train.loc[k,'sentiment'].upper(): continue #skip misclassified
    
    # PLOT INFLUENCE VALUE
    print()
    plt.figure(figsize=(20,3))
    idx = np.sum(att[k,])
    v = np.argsort(final_output[:idx-1])
    mx = final_output[v[-1]]; x = max(-10,-len(v))
    mn = final_output[v[x]]
    plt.plot(cha[k,:idx-2],final_output[1:idx-1],'o-')
    plt.plot([1,95],[mn,mn],':')
    plt.xlim((0,95))
    plt.yticks([]); plt.xticks([])
    plt.title('Train row %i. Predict %s.   True label is %s'%(k,pr[pred],train.loc[k,'sentiment']),size=16)
    plt.show()
    
    # DISPLAY ACTIVATION TEXT
    html = ''
    for j in range(1,idx):
        x = (final_output[j]-mn)/(mx-mn)
        html += "<span style='background:{};font-family:monospace'>".format('rgba(255,255,0,%f)'%x)
        html += tokenizer.decode( [ids[k,j]] )
        html += "</span>"
    html += " (predict)"
    display(HTML(html))

    # DISPLAY TRUE SELECTED TEXT
    text1 = " ".join(train.loc[k,'text'].lower().split()) 
    text2 = " ".join(train.loc[k,'selected_text'].lower().split())
    sp = text1.split(text2)
    html = "<span style='font-family:monospace'>"+sp[0]+"</span>"
    for j in range(1,len(sp)):
        html += "<span style='background:yellow;font-family:monospace'>"+text2+'</span>'
        html += "<span style='font-family:monospace'>"+sp[j]+"</span>"
    html += " (true)"
    display(HTML(html))
    print()
