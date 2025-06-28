import statsmodels.api as sm
class SimpleLinearRegression:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.x = sm.add_constant(x)

    def fit(self):
        model = sm.OLS(self.y, self.x).fit()
        return model

    def summary(self):
        model = self.fit()
        summary = model.summary()
        print(summary)
        return model
    
