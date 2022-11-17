from django.db import models

# Create your models here.

class Stock(models.Model):
    bookValue = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True)
    currentPrice = models.FloatField(null=True, blank=True)
    currentRatio = models.FloatField(null=True, blank=True)
    debtToEquity = models.FloatField(null=True, blank=True)
    dividendRate = models.FloatField(null=True, blank=True)
    dividendYield = models.FloatField(null=True, blank=True)
    enterpriseValue = models.BigIntegerField(null=True, blank=True)
    expectedReturn = models.FloatField(null=True, blank=True, default=None)
    exchange = models.CharField(max_length=100, null=True, blank=True)
    exchangeTimezoneName = models.CharField(max_length=100, null=True, blank=True)
    exchangeTimezoneShortName = models.CharField(max_length=100, null=True, blank=True)
    fairValue = models.FloatField(null=True, blank=True, default=0)
    financialCurrency = models.CharField(max_length=100, null=True, blank=True)
    fiveYearAvgDividendYield = models.FloatField(null=True, blank=True)
    forwardEps = models.FloatField(null=True, blank=True)
    forwardPE = models.FloatField(null=True, blank=True)
    freeCashflow = models.BigIntegerField(null=True, blank=True)
    fullTimeEmployees = models.BigIntegerField(null=True, blank=True)
    grossMargins = models.FloatField(null=True, blank=True)
    grossProfits = models.BigIntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    logo_url = models.CharField(max_length=100, null=True, blank=True)
    longName = models.CharField(max_length=100, null=True, blank=True)
    market = models.CharField(max_length=100, null=True, blank=True)
    marketCap = models.BigIntegerField(null=True, blank=True)
    mostRecentQuarter = models.BigIntegerField(null=True, blank=True)
    netIncomeToCommon = models.BigIntegerField(null=True, blank=True)
    openInterest = models.CharField(max_length=100, null=True, blank=True)
    operatingCashflow = models.BigIntegerField(null=True, blank=True)
    operatingMargins = models.FloatField(null=True, blank=True)
    payoutRatio = models.FloatField(null=True, blank=True)
    pegRatio = models.FloatField(null=True, blank=True)
    priceToBook = models.FloatField(null=True, blank=True)
    profitMargins = models.FloatField(null=True, blank=True)
    quickRatio = models.FloatField(null=True, blank=True)
    quoteType = models.CharField(max_length=100, null=True, blank=True)
    returnOnAssets = models.FloatField(null=True, blank=True)
    returnOnEquity = models.FloatField(null=True, blank=True)
    revenueGrowth = models.FloatField(null=True, blank=True)
    revenuePerShare = models.FloatField(null=True, blank=True)
    revenueQuarterlyGrowth = models.FloatField(null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    sharesOutstanding = models.BigIntegerField(null=True, blank=True)
    shortName = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    symbol = models.CharField(max_length=100, null=True, blank=True, unique=True)
    toCurrency = models.CharField(max_length=100, null=True, blank=True)
    totalAssets = models.CharField(max_length=100, null=True, blank=True)
    totalCash = models.BigIntegerField(null=True, blank=True)
    totalCashPerShare = models.FloatField(null=True, blank=True)
    totalDebt = models.BigIntegerField(null=True, blank=True)
    totalRevenue = models.BigIntegerField(null=True, blank=True)
    trailingAnnualDividendRate = models.FloatField(null=True, blank=True)
    trailingAnnualDividendYield = models.FloatField(null=True, blank=True)
    trailingEps = models.FloatField(null=True, blank=True)
    trailingPE = models.FloatField(null=True, blank=True)
    trailingPegRatio = models.FloatField(null=True, blank=True)
    twoHundredDayAverage = models.FloatField(null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    ytdReturn = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.symbol