"""
@Date: 2023/5/10 11:22
@Author: Jingtao Wang
@Version:1.0
"""
import folium


class mapSettings:
    def __init__(self):
        # 添加地点及对应经纬度坐标,负号表示西经和南纬
        self.map2loc_city = {"西昌": [27.899, 102.2626], "成都": [30.65984, 104.063365], "北京": [39.906, 116.391],
                             "雄安": [39.048, 115.907], "南宁": [22.82, 108.363], "乐山": [29.585, 103.748],
                             "郑州": [34.748, 113.62],"重庆": [29.565, 106.5466],"合肥":[31.868,117.28],
                             "南京": [32.0617, 118.7778],
                             "Toronto": [43.653, -79.385], "Buffalo": [42.886, -78.88]
                             }
        self.map2loc_pos = {"UB": [43.002, -78.785], "NiagaraFall": [43.256, -79.072], "CQPUT": [29.533532, 106.6042]}
        self.map_center = self.map2loc_city["成都"]  # 控制地图中心点的坐标为成都
        self.map = folium.Map(location=self.map_center, zoom_start=6)

    def add_loc_maker(self):
        # 添加标注
        for key in self.map2loc_city:
            folium.Marker(self.map2loc_city[key], popup=key).add_to(self.map)
        for key in self.map2loc_pos:
            folium.Marker(self.map2loc_pos[key], popup=key).add_to(self.map)


if __name__ == "__main__":
    m = mapSettings()
    m.add_loc_maker()
    # 保存地图
    m.map.save("map.html")
