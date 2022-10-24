def add_model_groups(tt):
    tt.loc[(tt['time'] > 0) & (tt['time'] <= 10), 'sbatch'] = 0
    tt.loc[(tt['time'] > 10) & (tt['time'] <= 50), 'sbatch'] = 1
    tt.loc[(tt['time'] > 50) & (tt['time'] <= 60), 'sbatch'] = 2
    tt.loc[(tt['time'] > 60) & (tt['time'] <= 100), 'sbatch'] = 3
    tt.loc[(tt['time'] > 100) & (tt['time'] <= 150), 'sbatch'] = 4
    tt.loc[(tt['time'] > 150) & (tt['time'] <= 200), 'sbatch'] = 5
    tt.loc[(tt['time'] > 200) & (tt['time'] <= 250), 'sbatch'] = 6
    tt.loc[(tt['time'] > 250) & (tt['time'] <= 300), 'sbatch'] = 7
    tt.loc[(tt['time'] > 300) & (tt['time'] <= 350), 'sbatch'] = 8
    tt.loc[(tt['time'] > 350) & (tt['time'] <= 400), 'sbatch'] = 9
    tt.loc[(tt['time'] > 400) & (tt['time'] <= 450), 'sbatch'] = 10
    tt.loc[(tt['time'] > 450) & (tt['time'] <= 500), 'sbatch'] = 11
    # Test
    tt.loc[(tt['time'] > 500) & (tt['time'] <= 510), 'sbatch'] = 12
    tt.loc[(tt['time'] > 510) & (tt['time'] <= 520), 'sbatch'] = 13
    tt.loc[(tt['time'] > 520) & (tt['time'] <= 530), 'sbatch'] = 14
    tt.loc[(tt['time'] > 530) & (tt['time'] <= 540), 'sbatch'] = 15
    tt.loc[(tt['time'] > 540) & (tt['time'] <= 550), 'sbatch'] = 16
    tt.loc[(tt['time'] > 550) & (tt['time'] <= 560), 'sbatch'] = 17
    tt.loc[(tt['time'] > 560) & (tt['time'] <= 570), 'sbatch'] = 18
    tt.loc[(tt['time'] > 570) & (tt['time'] <= 580), 'sbatch'] = 19
    tt.loc[(tt['time'] > 580) & (tt['time'] <= 590), 'sbatch'] = 20
    tt.loc[(tt['time'] > 590) & (tt['time'] <= 600), 'sbatch'] = 21
    tt.loc[(tt['time'] > 600) & (tt['time'] <= 610), 'sbatch'] = 22
    tt.loc[(tt['time'] > 610) & (tt['time'] <= 630), 'sbatch'] = 23
    tt.loc[(tt['time'] > 630) & (tt['time'] <= 650), 'sbatch'] = 24
    tt.loc[(tt['time'] > 650) & (tt['time'] <= 670), 'sbatch'] = 25
    tt.loc[(tt['time'] > 670) & (tt['time'] <= 700), 'sbatch'] = 26
    return tt

def had_drift(tt):
    """
    I dentify if section had drift in the original dataset
    """
    tt.loc[(tt['time'] > 0) & (tt['time'] <= 10), 'drift'] = False
    tt.loc[(tt['time'] > 10) & (tt['time'] <= 50), 'drift'] = False
    tt.loc[(tt['time'] > 50) & (tt['time'] <= 60), 'drift'] = True
    tt.loc[(tt['time'] > 60) & (tt['time'] <= 100), 'drift'] = False
    tt.loc[(tt['time'] > 100) & (tt['time'] <= 150), 'drift'] = False
    tt.loc[(tt['time'] > 150) & (tt['time'] <= 200), 'drift'] = False
    tt.loc[(tt['time'] > 200) & (tt['time'] <= 250), 'drift'] = False
    tt.loc[(tt['time'] > 250) & (tt['time'] <= 300), 'drift'] = False
    tt.loc[(tt['time'] > 300) & (tt['time'] <= 350), 'drift'] = True
    tt.loc[(tt['time'] > 350) & (tt['time'] <= 400), 'drift'] = True
    tt.loc[(tt['time'] > 400) & (tt['time'] <= 450), 'drift'] = True
    tt.loc[(tt['time'] > 450) & (tt['time'] <= 500), 'drift'] = True
    # Test
    tt.loc[(tt['time'] > 500) & (tt['time'] <= 510), 'drift'] = True
    tt.loc[(tt['time'] > 510) & (tt['time'] <= 520), 'drift'] = True
    tt.loc[(tt['time'] > 520) & (tt['time'] <= 530), 'drift'] = False
    tt.loc[(tt['time'] > 530) & (tt['time'] <= 540), 'drift'] = False
    tt.loc[(tt['time'] > 540) & (tt['time'] <= 550), 'drift'] = True
    tt.loc[(tt['time'] > 550) & (tt['time'] <= 560), 'drift'] = False
    tt.loc[(tt['time'] > 560) & (tt['time'] <= 570), 'drift'] = True
    tt.loc[(tt['time'] > 570) & (tt['time'] <= 580), 'drift'] = True
    tt.loc[(tt['time'] > 580) & (tt['time'] <= 590), 'drift'] = True
    tt.loc[(tt['time'] > 590) & (tt['time'] <= 600), 'drift'] = False
    tt.loc[(tt['time'] > 600) & (tt['time'] <= 610), 'drift'] = True
    tt.loc[(tt['time'] > 610) & (tt['time'] <= 630), 'drift'] = True
    tt.loc[(tt['time'] > 630) & (tt['time'] <= 650), 'drift'] = True
    tt.loc[(tt['time'] > 650) & (tt['time'] <= 670), 'drift'] = False
    tt.loc[(tt['time'] > 670) & (tt['time'] <= 700), 'drift'] = False
    return tt
