from electrum_dash.i18n import _

fullname = 'TREZOR Wallet'
description = _('Provides support for TREZOR hardware wallet')
requires = [('trezorlib','github.com/trezor/python-trezor')]
requires_wallet_type = ['trezor']
registers_wallet_type = ('hardware', 'trezor', _("TREZOR wallet"))
available_for = ['qt', 'cmdline']

