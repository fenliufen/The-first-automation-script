from test_api_pige.base_page import Base


class Operation(Base):


    def add_section(self,data):
        return self.send_api(data)


