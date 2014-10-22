import zlib
import base64


text = zlib.decompress(base64.b64decode('eJzFWcuS4yAMvO9XzM0Xl4szfAI1cIQ73KCKK' + \
                                        '5+/LQGOk9iOk2zVsjv7SGaittSSWuLn53+fP/8bwDcQFj7/A8IyK1VtSsI4gyPC1yjegYCHDtY4nN/b' + \
                                        'cT5KFQCqZPkZmssQYN0btu3MFgK/0l/2Wc7vw7gCYVnmnPST4Ucc8A+C47Wt6p9CWKZQhfbGuFME/d0' + \
                                        'GA8FJ5TpHXkBYIojn8aF8zI4n3HjLGO+1vkE15SKIEwiLCiFbnWoV9GSGfbGxSoY9vWa8EEJrYXG89y' + \
                                        'tMEy+BOIYgk7A1eZFiiUlo/IKd9pzGkEFY9XjR2oTfFc6iZPm9C5ievoEgEQE8N8x5YTX9mWKMOTMet' + \
                                        'gbmwfV4crwr6E/3GKDf3/IxhCWUaukjh7e9qKXESJmP/MC7QuM1b7SoMQGJgCv8HWXbv8WFUBxAKFav' + \
                                        'HBR4+IkMh03SL8tEiSqKmmVMwFcAWgj/UDmcfR2Kg0AslhFw7ZtaJ1jmp7IzSXoTaOZ5AndDztEyV7w' + \
                                        '21+lwAEG2j3AiTBdaETcs9A4ZMvlC9+zkWLj4IYTAP+2rmq9A+GmuUFJKxoBc0cwgPIjTr2rlLgRmAr' + \
                                        'iU1TRdaciMoEGAH4ieMO7YF0iWV5HYg6Aam0xU80VN0PhAEGQoaRQn7hnmJSF3IICKHAYd5XwFQdMuU' + \
                                        '8cQcvX39eGVG54hUDKwE0QN6jwOMKwCahWSEslQa02JirR46CR6fhdC4mxw2qYYpn15RgkgmfzPjctR' + \
                                        'HMxdRzv3wz4X2AkDQvf05tCzJ33WvcHFTTj8qRv2IEyevZBiVoPlBZ7OOQSJLJ3mcC5gHFVJc+uYv/4' + \
                                        '0L/cghB6IGqlNtxJz687av9RPmgvCrWmHMwS7EEr7oBeGLh93jmAXQuQf9NbsfyQEygk68/imE+cJsQ' + \
                                        '+BHOCt3zWkSRROxe+9xwC186RjxHgAY7M6rS2HGXF0uiKc9cPD335Gg7gQF+MbHCCdysj9HnGMwAxlP' + \
                                        'NV9oE5kziBSMuCyrzl6e+qGXQhLPQq2s+vItMi0Fw1TAzuBj0c8o6JW8y6Ezsido8vQLVSilN2pjbHF' + \
                                        'ocZYciRhnV902wMI866Xnaj5BoHac04QB6ijNZJ0g2F0C/JCbBAU5F1Bx58+gfDsYyci9Ejun9ZL9Zx' + \
                                        'hUs4kK3qrZP3WvMCSE/YnZc9Kw4F8vSODI/1M7QLKrIS5tWY1k+EpZK7cUio6DcDKhdy7nMrve4Gd0A' + \
                                        'qzoF7VXp1kqNDr9HyxJg5ADNS0MrWQ0E7eQmhwXyiOg0DU34ZBb/Gr3h3dGOuQIDMLJklGey9bIdSKP' + \
                                        'kfpcI7gUL56bk2mbvOpbPoTLzYwWUx8KEL02MzJ1Qu1huWC+j2aI4KgBzVpI+IXu+a+XcUM841pSGmw' + \
                                        'OoKTo8YrI+XxTBmo3xrSj8PYVCzrAFGI6Df9gkwADVdNQfY5P6HnLu06jifrGdxzxpag2NeskWFLSp4' + \
                                        't4HskgaT/k6hhBKVRsjMhAUL+DgJNlphba5Yt4ORtqChFM61IJFRpbIKGwbhgWcByVgwukpBNlxYM51' + \
                                        'uWCAiF58bBON558dRIOUl6OfFQm0cgCABLaUFF83sIi6ZITKRgUYSq7msFMouSPLRkq4uB0rKVDPYQQ' + \
                                        'UxXyPBi15SNT6W12kXSwFCpMDXjVB9bAZ5opM2tFrB9CpEXtlb5PYSfEK0FBgKB0YGIR4yYySYd1eqy' + \
                                        '7K0pJR5paQNFa5l6iY+v947Bi9jWCIDAHm+0a7Hf5gAoyPtBVt1G02LoytbtJYQlGijZSI4PrRXkXgh' + \
                                        'XALnXQiBoKy9ubZao8U8goFBqqlE0VfBqjehAJYCDoua22chUiuxm6+gxCFGpuFAfLy2AA6kj5zXRHL' + \
                                        'mGJCSNMBMNZq5XTIQNAlq/tl4hX4/mF9fgWbT9m9GskDJhoCzgwLSZWvhVaSEIo1LnktBRoDK+hkC7W' + \
                                        'N3lC9KdE5O9X9c0vG3ZUM46Ryh7i2g999AZb9xHLNk3ncBFmZAg+vRPv904UgwGTfnvjFbjkSniSDq9' + \
                                        'dSujtsMarXGetT4B6GfIqEhbUlrP6v38ePNiaJL2yeoWgB2qhVOGSxm4zHtydBSd9hLk7bspdThNUil' + \
                                        'oqqUMALz+Yo2hG4gUn3n5/g2dPMBgbO3ajXchspfwyEq4dVZuq0+d630Ii9h1AdfjVjTD6gIgMMNFtL' + \
                                        'O36FzrKPI5hF03GFtHE2UajhaWb99rWhIlW7nh4rsD7ZHU9MlVqRSP455vdTsO7RYaAinvPUZbPPBBC' + \
                                        'E+5jMbDI/hnt7X5/vZDpw5gbV09DOURKwseVnyxSaxS62cQtnxAItRBxBVCYGFb9mjj2kUPSjw6L4pn' + \
                                        '/hBCuq3ToEziMwQ65W412e8GBjn5Mq3CEeEDCHMqYSwWXNORNcY1IXOfdIu9r559bThQ/Lp+rag/yYj' + \
                                        'bB9O1WBoEvzmCalPcyZsVBbc7uvHDl/mqLjjdVHxKq7Bt9RlfaW9XxKNw03XCtqsT7f78Be+xUVE='))

if __name__ == '__main__':
	print text
