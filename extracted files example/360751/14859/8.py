opts = {'cmap': 'Paired',
        'yticks': list(range(0,300,50)),
        'colorbar': False,
       'grid': True,
         }

land_ne = tt[(tt.IntersectionId == 2) &
             (tt.EntryStreetName == 'Land Boulevard') &
             (tt.ExitHeading == 'NE')
             ].join(target_df)
landplot = land_ne.hvplot.scatter('Hour', 'TimeFromFirstStop_p80', 
                                    c='Weekend', **opts)

cambria_e = tt[(tt.IntersectionId == 1824) &
             (tt.EntryStreetName == 'West Cambria Street') &
             (tt.ExitHeading == 'E')
             ].join(target_df)
cambplot = cambria_e.hvplot.scatter('Hour', 'TimeFromFirstStop_p80', 
                                    c='Weekend', **opts)

display(landplot.options(title='Land_NE_thru'), cambplot.options(title='Cambria_E_thru'))
