import facebook

# Access token phải là PAGE TOKEN
access_token = "EAAIsE61mR9QBO6v3eIbeQf04N6eFuYqD1hDv7kqFtGLXzuJ92hzJF2QOZBhjCn8CBDSuWmYaJyV1OnXvY2lsDosa3jbv6yDaawkp6iOhfLC1vW75SKwgLyIUtnkFPoGp4JbEs2y3XLilCpH6C5XXZCknRVK7CXfVnPuImye8uBZBq09muUTvYPpAchjJ1p0nLHJ9cyqMYypGtCLaO0Gd9oSdgZDZD"  # thay bằng token bạn lấy được

# Tạo đối tượng Graph API
graph = facebook.GraphAPI(access_token)

# Đăng bài lên Trang (dùng 'me' nếu access token là của Page)
graph.put_object(parent_object='me', connection_name='feed', message='tooi laf viet ')