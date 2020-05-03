
class Piece(object):
    # 棋子类
    def __init__(self, count, color, position):
        self.count = count  # 当前步数，第几颗棋子（不区分黑白）
        self.color = color  # 棋子颜色， 1为黑， 0为白
        self.position = position  # 棋子位置，位置坐标为(0, 0)-(18, 18)


class StepRecordChessBoard(object):
    # 棋盘状态类
    def __init__(self, first, level):
        """
        初始化棋盘记录
        初始化AI
        :param first: 先手方
        """
        self.count = 0  # 棋盘初始步数为0
        self.records = [[None for i in range(19)] for j in range(19)]  # 棋盘初始化为19*19的0矩阵

        # first = 1 黑方先手， first = 0 白方先手
        self.first = first


        # 数组记录
        self.list1 = []  # 记录白棋坐标数组
        self.list2 = []  # 记录黑棋坐标数组
        self.list3 = []  # 记录所有棋子坐标数组

        # 策略记录
        self.next_point = [0, 0]
        self.cut_count = 0  # 统计剪枝次数
        self.search_count = 0  # 统计搜索次数

        # 策略记录
        self.col = 19  # 占位暂定
        self.row = 19  # 占位暂定
        self.depth = level  # 搜索深度，即AI的远见程度，搜索深度为3即AI能看3步布局
        self.strategy = 1  # 策略系数，大于1为进攻型策略，小于1为保守型策略
        self.shape_score = [(50, (0, 1, 1, 0, 0)),  # 各种棋型的评估分数（score， shape）
                            (50, (0, 0, 1, 1, 0)),
                            (200, (1, 1, 0, 1, 0)),
                            (500, (0, 0, 1, 1, 1)),
                            (500, (1, 1, 1, 0, 0)),
                            (5000, (0, 1, 1, 1, 0)),
                            (5000, (0, 1, 0, 1, 1, 0)),
                            (5000, (0, 1, 1, 0, 1, 0)),
                            (5000, (1, 1, 1, 0, 1)),
                            (5000, (1, 1, 0, 1, 1)),
                            (5000, (1, 0, 1, 1, 1)),
                            (5000, (1, 1, 1, 1, 0)),
                            (5000, (0, 1, 1, 1, 1)),
                            (50000, (0, 1, 1, 1, 1, 0)),
                            (99999999, (1, 1, 1, 1, 1))]

    def has_record(self, x, y):
        """
        :param x: 棋子横坐标
        :param y: 棋子纵坐标
        :return: 返回某处是否已经落子,1为已经落子，0为没有落子
        """
        if self.records[x][y]:
            return 1
        else:
            return 0

    def insert_record(self, x, y):
        """

        :param x: 棋子横坐标
        :param y: 棋子纵坐标
        """
        self.count += 1
        if self.first == 1:
            # 黑方先手
            self.records[x][y] = Piece(self.count, self.count % 2, [x, y])
            print('{0}'.format('white' if self.count % 2 == 0 else 'black'), '< x:', x, ', y:', y, '>')
        else:
            # 白方先手
            self.records[x][y] = Piece(self.count, (self.count + 1) % 2, [x, y])
            print('{0}'.format('white' if (self.count + 1) % 2 == 0 else 'black'), '< x:', x, ', y:', y, '>')

    def who_play(self):
        """

        :return:返回值为1黑棋走，返回值为0白棋走
        """
        if self.first == 1:
            return self.count % 2
        else:
            return (self.count + 1) % 2

    def check_row(self, x, y):
        """
        检测一行中是否有连续的5个子
        :param x: 棋子横坐标
        :param y: 棋子纵坐标
        :return: 
        """
        if self.has_record(x, y) and self.has_record(x + 1, y) and self.has_record(x + 2, y) and self.has_record(x + 3,
                                                                                                                 y) and self.has_record(
                        x + 4, y):

            if self.records[x][y].color == 1 and self.records[x + 1][y].color == 1 and self.records[x + 2][
                y].color == 1 and self.records[x + 3][y].color == 1 and self.records[x + 4][y].color == 1:
                # 黑棋获胜
                return 1

            elif self.records[x][y].color == 0 and self.records[x + 1][y].color == 0 and self.records[x + 2][
                y].color == 0 and self.records[x + 3][y].color == 0 and self.records[x + 4][y].color == 0:
                # 白棋获胜
                return 0
            else:
                return -1

        else:
            # 无人获胜
            return -1

    def check_col(self, x, y):
        """
        检测一列中是否有连续的5个子
        :param x:棋子横坐标
        :param y:棋子纵坐标
        :return:
        """
        if self.has_record(x, y) and self.has_record(x, y + 1) and self.has_record(x, y + 2) and self.has_record(x,
                                                                                                                 y + 3) and self.has_record(
                x, y + 4):

            if self.records[x][y].color == 1 and self.records[x][y + 1].color == 1 and self.records[x][
                        y + 2].color == 1 and self.records[x][y + 3].color == 1 and self.records[x][y + 4].color == 1:
                # 黑棋胜利
                return 1

            elif self.records[x][y].color == 0 and self.records[x][y + 1].color == 0 and self.records[x][
                        y + 2].color == 0 and self.records[x][y + 3].color == 0 and self.records[x][y + 4].color == 0:
                # 白棋胜利
                return 0
            else:
                return -1

        else:
            return -1

    def check_up(self, x, y):
        """

        检测\斜线方向是否有连续的子
        :param x:
        :param y:
        :return:
        """
        if self.has_record(x, y) and self.has_record(x + 1, y + 1) and self.has_record(x + 2,
                                                                                       y + 2) and self.has_record(x + 3,
                                                                                                                  y + 3) and self.has_record(
                        x + 4, y + 4):

            if self.records[x][y].color == 1 and self.records[x + 1][y + 1].color == 1 and self.records[x + 2][
                        y + 2].color == 1 and self.records[x + 3][y + 3].color == 1 and self.records[x + 4][
                        y + 4].color == 1:
                return 1

            elif self.records[x][y].color == 0 and self.records[x + 1][y + 1].color == 0 and self.records[x + 2][
                        y + 2].color == 0 and self.records[x + 3][y + 3].color == 0 and self.records[x + 4][
                        y + 4].color == 0:
                return 0
            else:
                return -1

        else:
            return -1

    def check_down(self, x, y):

        """
        检测/斜线方向是否有连续的子
        :param x: 
        :param y: 
        :return: 
        """
        if self.has_record(x, y) and self.has_record(x + 1, y - 1) and self.has_record(x + 2,
                                                                                       y - 2) and self.has_record(x + 3,
                                                                                                                  y - 3) and self.has_record(
                        x + 4, y - 4):

            if self.records[x][y].color == 1 and self.records[x + 1][y - 1].color == 1 and self.records[x + 2][
                        y - 2].color == 1 and self.records[x + 3][y - 3].color == 1 and self.records[x + 4][
                        y - 4].color == 1:
                return 1

            elif self.records[x][y].color == 0 and self.records[x + 1][y - 1].color == 0 and self.records[x + 2][
                        y - 2].color == 0 and self.records[x + 3][y - 3].color == 0 and self.records[x + 4][
                        y - 4].color == 0:
                return 0
            else:
                return -1

        else:
            return -1

    def check_victory(self):
        """

        遍历棋盘，判断是否胜利
        :return 返回值为1黑棋胜利，返回值为0白棋胜利，返回值为-1无人胜利
        """
        for i in range(15):
            for j in range(19):
                result = self.check_row(i, j)
                if result != -1:
                    return result

        for i in range(19):
            for j in range(15):
                result = self.check_col(i, j)
                if result != -1:
                    return result

        for i in range(15):
            for j in range(15):
                result = self.check_up(i, j)
                if result != -1:
                    return result

        for i in range(15):
            for j in range(4, 19):
                result = self.check_down(i, j)
                if result != -1:
                    return result

        return -1

    def insert_position_list(self, color, position):
        if color == 1:
            self.list1.append(position)
        else:
            self.list2.append(position)
        self.list3.append(position)

    def cal_score(self, m, n, x_depend, y_depend, enemy_list, my_list, score_all_arr):

        """

        :param m: 棋子x坐标
        :param n: 棋子y坐标
        :param x_depend: 棋子x方向延伸判断
        :param y_depend: 棋子y方向延伸判断
        :param enemy_list: 敌人棋子位置列表
        :param my_list: 我方棋子位置列表
        :param score_all_arr: 交叉棋型记录
        :return: 当前棋型得分，即得分项和加分项之和
        """
        # 在一个方向上， 只取最大的得分项
        max_score_shape = (0, None)

        # 如果此方向上，该点已经有得分形状，不重复计算
        for item in score_all_arr:
            for pt in item[1]:
                if m == pt[0] and n == pt[1] and x_depend == item[2][0] and y_depend == item[2][1]:
                    return 0
        # 计算得分项
        # 在落子点 左右方向上循环查找得分形状
        for offset in range(-5, 1):
            # pos = 2 有对方棋子
            # pos = 1 有我方棋子
            # pos = 0 无棋子
            pos = []
            for i in range(0, 6):
                if (m + (i + offset) * x_depend, n + (i + offset) * y_depend) in enemy_list:
                    pos.append(2)
                elif (m + (i + offset) * x_depend, n + (i + offset) * y_depend) in my_list:
                    pos.append(1)
                else:
                    pos.append(0)
            # print("pos:",pos)
            tmp_shap5 = (pos[0], pos[1], pos[2], pos[3], pos[4])
            tmp_shap6 = (pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

            for (score, shape) in self.shape_score:
                if tmp_shap5 == shape or tmp_shap6 == shape:
                    if tmp_shap5 == (1, 1, 1, 1, 1):
                        print('!!!')
                    if score > max_score_shape[0]:
                        # 标记为最好棋型
                        # max_score_shape =
                        max_score_shape = (score, ((m + (0 + offset) * x_depend, n + (0 + offset) * y_depend),
                                                   (m + (1 + offset) * x_depend, n + (1 + offset) * y_depend),
                                                   (m + (2 + offset) * x_depend, n + (2 + offset) * y_depend),
                                                   (m + (3 + offset) * x_depend, n + (3 + offset) * y_depend),
                                                   (m + (4 + offset) * x_depend, n + (4 + offset) * y_depend)),
                                           (x_depend, y_depend))

        # 计算加分项
        # 计算两个形状相交， 如两个3活 相交， 得分增加 一个子的除外
        add_score = 0  # 加分项
        if max_score_shape[1] is not None:
            print(score_all_arr)
            for item in score_all_arr:
                for pt1 in item[1]:
                    for pt2 in max_score_shape[1]:
                        if pt1 == pt2 and max_score_shape[0] > 10 and item[0] > 10:
                            add_score += item[0] + max_score_shape[0]

            score_all_arr.append(max_score_shape)

        return add_score + max_score_shape[0]  # 最终结果为得分项+加分项

    def evaluation(self, is_ai):
        # 判断是哪一方进行判定
        if is_ai:
            my_list = self.list1
            enemy_list = self.list2
        else:
            my_list = self.list2
            enemy_list = self.list1

        # 算自己的得分
        score_all_arr = []  # 用于标记双三等交叉棋型
        my_score = 0
        for position in my_list:
            m = position[0]
            n = position[1]
            my_score += self.cal_score(m, n, 0, 1, enemy_list, my_list, score_all_arr)
            my_score += self.cal_score(m, n, 1, 0, enemy_list, my_list, score_all_arr)
            my_score += self.cal_score(m, n, 1, 1, enemy_list, my_list, score_all_arr)
            my_score += self.cal_score(m, n, -1, 1, enemy_list, my_list, score_all_arr)

        # 算敌人的得分， 并减去
        score_all_arr_enemy = []
        enemy_score = 0
        for pt in enemy_list:
            m = pt[0]
            n = pt[1]
            enemy_score += self.cal_score(m, n, 0, 1, my_list, enemy_list, score_all_arr_enemy)
            enemy_score += self.cal_score(m, n, 1, 0, my_list, enemy_list, score_all_arr_enemy)
            enemy_score += self.cal_score(m, n, 1, 1, my_list, enemy_list, score_all_arr_enemy)
            enemy_score += self.cal_score(m, n, -1, 1, my_list, enemy_list, score_all_arr_enemy)

        total_score = my_score - enemy_score * self.strategy * 0.1

        return total_score

    def has_neighbor(self, position):

        """

        :param position: 棋子位置坐标
        :return: True 有邻居 False 无邻居
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (position[0] + i, position[1] + j) in self.list3:
                    return True
        return False

    def negative_max(self, is_ai, depth, alpha, beta):
        """
        使用α-β剪枝的负值极大算法
        :param is_ai: 是否为AI
        :param depth: AI搜索深度
        :param alpha: 初始最小奖励
        :param beta: 初始最大奖励
        :return: 规划最大奖励 alpha

        """
        # 游戏是否结束 | | 探索的递归深度到边界 -> 退出递归
        if self.check_victory() == 1 or self.check_victory() == 0 or depth == 0:
            return self.evaluation(is_ai)

        # 棋盘上未落子的列表
        list_all = []
        for i in range(19):
            for j in range(19):
                list_all.append((i, j))
        blank_list = []
        for item in list_all:
            if item not in self.list3:
                blank_list.append(item)
        for item in self.list3:
            if item not in list_all:
                blank_list.append(item)
        print('blank_list_old:', blank_list[0])
        self.order(blank_list)  # 搜索顺序排序  提高剪枝效率
        print('blank_list_new:', blank_list[0])

        # 遍历每一个候选步
        for next_step in blank_list:

            self.search_count += 1  # 搜索次数

            # 如果要评估的位置没有相邻的子，则略过
            if not self.has_neighbor(next_step):
                continue

            if is_ai:
                self.list1.append(next_step)
            else:
                self.list2.append(next_step)
            self.list3.append(next_step)

            value = -self.negative_max(not is_ai, depth - 1, -beta, -alpha)
            if is_ai:
                self.list1.remove(next_step)
            else:
                self.list2.remove(next_step)
            self.list3.remove(next_step)

            if value > alpha:
                # 数据显示
                print(str(value) + "alpha:" + str(alpha) + "beta:" + str(beta))
                print(self.list3)
                if depth == self.depth:
                    self.next_point[0] = next_step[0]
                    self.next_point[1] = next_step[1]
                # alpha + beta剪枝点
                if value >= beta:
                    self.cut_count += 1  # 剪枝次数
                    return beta
                alpha = value
        return alpha

    def order(self, blank_list):
        """
        提前遍历棋盘上未置棋子的部分，将最后一子的邻居棋子放在优先级较高的地方优先遍历
        :param blank_list:棋盘上空棋子集合
        """
        last_pt = self.list3[-1]
        for item in blank_list:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:  # 该棋子本身
                        continue
                    if (last_pt[0] + i, last_pt[1] + j) in blank_list:  # 邻居棋子
                        blank_list.remove((last_pt[0] + i, last_pt[1] + j))
                        blank_list.insert(0, (last_pt[0] + i, last_pt[1] + j))

    def policy_decision(self):
        """
        AI决策函数
        :return: next_point AI下一步落子位置
        """
        self.cut_count = 0  # 初始化剪枝次数
        self.search_count = 0  # 初始化搜索次数
        self.negative_max(True, self.depth, -99999999, 99999999)  # 起始最大最小为正负无穷
        print("本次共剪枝次数：" + str(self.cut_count))
        print("本次共搜索次数：" + str(self.search_count))
        return self.next_point[0], self.next_point[1]

    def isForbidden(self, x, y, rid):
        # 禁手规则
        # 判断禁手
        # 1．三、三禁手
        # 黑方一子落下同时形成两个或两个以上的活三（或嵌四），此步为三三禁手。 注意：这里一定要两个都是 “活”三才能算。
        # 2．四、四禁手
        # 黑方一子落下同时形成两个或两个以上的四，活四、冲四、嵌五之四，包括在此四之内。此步为四四禁手。注意：只要是两个“四”即为禁手，无
        # 论是哪种四，活四，跳四，冲四都算。
        # 3．四、三、三禁手
        # 黑方一步使一个四，两个活三同时形成。
        # 4．四、四、三禁手
        # 黑方一步使两个四，一个活三同时形成。
        # 5．长连禁手
        # 黑方一子落下形成连续六子或六子以上相连
        chessboard = self.records

        # 竖直方向
        tCount = 0  # 活三个数
        fCount = 0  # 四子个数
        count = 1  # 棋子个数
        emptyCount = 0
        i = x
        j = y
        for loop in range(1, 6):
            if j - loop < 0:
                break
            if not chessboard[i][j - loop] and not emptyCount:
                emptyCount += 1
            elif chessboard[i][j - loop] == type:
                count += 1
            else:
                break
        j = y
        for loop in range(1, 6):
            if j + loop > 14:
                break
            if not chessboard[i][j + loop] and not emptyCount:
                emptyCount += 1
            elif chessboard[i][j + loop] == type:
                count += 1
            else:
                break
        if count == 3:
            tCount += 1
        elif count == 4:
            fCount += 1
        elif count > 5:
            return True

        # 水平方向
        count = 1  # 棋子个数
        emptyCount = 0
        i = x
        j = y
        for loop in range(1, 6):
            if i - loop < 0:
                break
            if not chessboard[i - loop][j] and not emptyCount:
                emptyCount += 1
            elif chessboard[i - loop][j] == type:
                count += 1
            else:
                break
        i = x
        for loop in range(1, 6):
            if i + loop > 14:
                break
            if not chessboard[i + loop][j] and not emptyCount:
                emptyCount += 1
            elif chessboard[i + loop][j] == type:
                count += 1
            else:
                break
        if count == 3:
            tCount += 1
        elif count == 4:
            fCount += 1
        elif count > 5:
            return True

        # 左下右上方向
        count = 1  # 棋子个数
        emptyCount = 0
        i = x
        j = y
        for loop in range(1, 6):
            if j + loop > 14 or i - loop < 0:
                break
            if not chessboard[i - loop][j + loop] and not emptyCount:
                emptyCount += 1
            elif chessboard[i - loop][j + loop] == type:
                count += 1
            else:
                break
        i = x
        j = y
        for loop in range(1, 6):
            if i + loop > 14 or j - loop < 0:
                break
            if not chessboard[i + loop][j - loop] and not emptyCount:
                emptyCount += 1
            elif chessboard[i + loop][j - loop] == type:
                count += 1
            else:
                break
        if count == 3:
            tCount += 1
        elif count == 4:
            fCount += 1
        elif count > 5:
            return True

        # 左上右下方向
        count = 1  # 棋子个数
        emptyCount = 0
        i = x
        j = y
        for loop in range(1, 6):
            if j - loop < 0 or j - loop < 0:
                break
            if not chessboard[i - loop][j - loop] and not emptyCount:
                emptyCount += 1
            elif chessboard[i - loop][j - loop] == type:
                count += 1
            else:
                break
        i = x
        j = y
        for loop in range(1, 6):
            if i + loop > 14 or j + loop > 14:
                break
            if not chessboard[i + loop][j + loop] and not emptyCount:
                emptyCount += 1
            elif chessboard[i + loop][j + loop] == type:
                count += 1
            else:
                break
        if count == 3:
            tCount += 1
        elif count == 4:
            fCount += 1
        elif count > 5:
            return True

        # 结果判断
        if tCount == 2 and not fCount:
            return True
        elif tCount == 2 and fCount == 1:
            return True
        elif tCount == 1 and fCount == 2:
            return True
        elif not tCount and fCount == 2:
            return True
        return False




