from  db.news_dao import NewsDao
class NewService:
    __new_dao=NewsDao()
    #查询待审批新闻列表
    def search_unreview_list(self,page):
        result=self.__new_dao.search_unreview_list(page)
        return result
    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        count_page=self.__new_dao.search_unreview_count_page()
        return count_page

    #审批新闻
    def update_unreview_news(self,id):
        self.__new_dao.update_unreview_news(id)

    # 查看新闻列表
    def search_list(self, page):
        result=self.__new_dao.search_list(page)
        return result

    #查询新闻总页数
    def serach_count_page(self):
        result=self.__new_dao.serach_count_page()
        return result

    #根据id删除新闻
    def delete_by_id(self,id):
        self.__new_dao.delete_by_id(id)
