import xmindparser
import pandas as pd
from uuid import uuid4
from openpyxl.worksheet.datavalidation import DataValidation


def parse_testcase(topic, parent_id=None):
    """解析单个测试用例节点"""
    case_id = str(uuid4())[:8]  # 生成8位唯一ID
    title = topic.get('title', '')
    notes = topic.get('note', '').split('|')

    # 从标签提取优先级和类型（示例标签：[P0][功能测试]）
    labels = topic.get('labels', [])
    priority = next((l[1:-1] for l in labels if l.startswith('[') and 'P' in l), 'P2')
    test_type = next((l[1:-1] for l in labels if l.startswith('[') and not 'P' in l), '功能测试')

    # 提取前置条件和测试数据
    precondition = notes[0].strip() if len(notes) > 0 else ''
    test_data = notes[1].strip() if len(notes) > 1 else ''

    base_case = {
        '用例ID': case_id,
        '用例名称': title,
        '优先级': priority,
        '测试类型': test_type,
        '前置条件': precondition,
        '测试数据': test_data
    }

    # 处理测试步骤
    steps = []
    for idx, step in enumerate(topic.get('topics', []), 1):
        step_title = step.get('title', '')
        expected_result = step.get('topics', [{}])[0].get('title', '') if step.get('topics') else ''

        steps.append({
        ** base_case,
        '步骤序号': idx,
        '操作步骤': step_title,
        '预期结果': expected_result,
        '实际结果': '',  # 预留执行记录字段
        '测试状态': '未执行'
        })

        return steps

    def xmind_testcase_to_excel(xmind_path, excel_path):
        """测试用例专用转换函数"""
        content = xmindparser.parse(xmind_path)
        all_steps = []

        # 遍历每个测试套件
        for sheet in content:
            root_topic = sheet['topic']
            for case in root_topic.get('topics', []):
                all_steps.extend(parse_testcase(case))

        # 生成DataFrame
        df = pd.DataFrame(all_steps)
        columns_order = [
            '用例ID', '用例名称', '优先级', '测试类型',
            '前置条件', '测试数据', '步骤序号',
            '操作步骤', '预期结果', '实际结果', '测试状态'
        ]

        # 导出Excel
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            df[columns_order].to_excel(writer, index=False)

            # 添加数据有效性验证
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']

            # 添加下拉列表（示例：测试状态列）
            dv = DataValidation(type="list", formula1='"未执行,通过,失败,阻塞"', allow_blank=True)
            worksheet.add_data_validation(dv)
            dv.add('L2:L1048576')  # 假设测试状态在L列

    if __name__ == '__main__':
        xmind_testcase_to_excel('testcases.xmind', 'testcases.xlsx')