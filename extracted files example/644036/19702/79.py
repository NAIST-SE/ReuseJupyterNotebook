myplace = "US_Florida"
tt.query('Place == @myplace and Days_Since_First_Fatal >= 0')[['Days_Since_First_Fatal','Fatalities_Log']]
