#To convert Country Code to object so that it won't sum it up and be classified as numerical column
data['Country Code'] = data['Country Code'].astype(object)

#Dropping missing values
data.dropna(inplace=True)

# Replacing the outlier with the average rating, what's the total average rating
averagerating = data[data['Aggregate rating'] != 0]['Aggregate rating'].mean()
#Replacing any occurenece of 0 with the average rating
data['Aggregate rating'] = np.where(df['Aggregate rating']==0, averagerating, df['Aggregate rating'])

data.head()
