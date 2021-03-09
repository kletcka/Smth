from additional_file import check

def test():     
    assert check('capybara@capy.bara') == True
    assert check('capybara@capy.ba.ra')  == True
    assert check('capybara.capy.bara') == False
    assert check('capybara@capy@bara') == False
    assert check('capybara!@capy.bara')  == False
    assert check('капибара@capy.bara')  == False
    assert check('capy bara@capy.bara')  == False
    assert check('capybara@capy')  == False
    assert check('capybara@c.apybara')  == False
    assert check('capybara@capy.ba.ra1')  == False
    assert check('capybara@ca.pybara')  == False
    assert check('capybara@capybar.a')  == False
    assert check('capybara@cap')  == False