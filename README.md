
# Python Calculate Sample

一个最小可用示例：提供 `calculate(expression: str)` 函数，支持加减乘除与括号，
并内置 GitHub Actions：

- **CI**：在 push / PR 时自动运行 pytest（云端单元验证）。
- **Release**：当打 tag（例如 `v1.0.0`）时自动构建包并创建 GitHub Release，上传构建产物。

## 本地运行

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt

# 运行测试
pytest -q --disable-warnings --maxfail=1
```

## 函数说明

```python
from calcpkg import calculate
print(calculate("1 + 2 * (3 - 1) / 4"))  # 2.0
```

- 支持运算符：`+ - * /`
- 支持括号：`()`
- 会对非法字符与非法表达式抛出 `ValueError`

## 推送到 GitHub 并触发 CI

1. 在 GitHub 新建一个空仓库。
2. 本地执行：
   ```bash
   git init
   git add .
   git commit -m "init: calculate sample"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
3. 打开仓库 **Actions** 页签查看 CI 运行结果。

## 触发发布（Release）

当你给仓库打上 tag（例如 `v1.0.0`）并 push：

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions 会：
- 运行测试
- 构建 wheel 与 sdist
- 创建 GitHub Release 并上传构建产物

## 目录结构

```text
python-calculate-sample/
├─ src/calcpkg/
│  ├─ __init__.py
│  └─ core.py            # calculate 实现
├─ tests/test_calculate.py
├─ .github/workflows/ci-release.yml
├─ pyproject.toml        # 打包配置
├─ requirements-dev.txt  # 本地与 CI 依赖
├─ setup.cfg             # pytest 配置
├─ .gitignore
└─ README.md
```
