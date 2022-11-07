import streamlit as st
st.title('hola')
df = pd.read_csv('https://raw.githubusercontent.com/napoles-uach/covid19mx/master/meteorite-landings.csv')
#st.write(df)

#fig = px.scatter_mapbox(df, lat=df['reclat'], lon=df['reclong'],center={'lat':28.63527778,'lon':-106.0888889})
#fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(title = 'Ejemplo:Chihuahua')
#st.write(fig)

#mass = df['mass'].tolist()
#year = df['year'].tolist()

#fig, ax = plt.subplots()
#ax.scatter(mass,year)
#ax.set_xlim([1000, 2000])
#ax.set_ylim([1900, 2000])
#st.pyplot(fig)
