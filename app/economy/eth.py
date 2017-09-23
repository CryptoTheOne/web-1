'''
    Copyright (C) 2017 Gitcoin Core 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
from django.conf import settings
import json
from web3 import Web3
from web3.providers.rpc import KeepAliveRPCProvider, HTTPProvider


def getWeb3(provider='default'):
    if provider == 'infura':
        host = 'mainnet.infura.io' if not settings.IS_TESTNET else 'ropsten.infura.io'
        web3 = Web3(HTTPProvider('https://mainnet.infura.io/'+settings.INFURA_KEY))
    elif provider == 'cusom_provider' and settings.DEBUG:
        web3 = Web3(KeepAliveRPCProvider(host=settings.GETH_HOST, port=8545))
    elif provider == 'testrpc_internal' and settings.DEBUG:
        web3 = Web3(KeepAliveRPCProvider(host='localhost', port=8545))
    elif provider == 'testrpc' and settings.DEBUG:
        web3 = Web3(KeepAliveRPCProvider(host='localhost', port=8545))
    else:
        web3 = Web3(KeepAliveRPCProvider(host=settings.GETH_HOST, port=settings.GETH_PORT))
    return web3


# http://web3py.readthedocs.io/en/latest/contracts.html
def getBountyContract(web3):
    abi_str = '[{"inputs": [{"type": "uint256", "name": ""}], "constant": true, "name": "bounty_indices", "outputs": [{"type": "bytes32", "name": ""}], "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": ""}], "constant": true, "name": "bountiesbyrepo", "outputs": [{"type": "uint256", "name": ""}], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "str"}], "constant": false, "name": "normalizeIssueURL", "outputs": [{"type": "string", "name": "result"}], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "str"}], "constant": false, "name": "getRepoURL", "outputs": [{"type": "string", "name": "result"}], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_issueURL"}, {"type": "uint256", "name": "_amount"}, {"type": "address", "name": "_tokenAddress"}, {"type": "uint256", "name": "_expirationTimeDelta"}, {"type": "string", "name": "_metaData"}], "constant": false, "name": "postBounty", "outputs": [{"type": "bool", "name": ""}], "payable": true, "type": "function"}, {"inputs": [], "constant": true, "name": "numBounties", "outputs": [{"type": "uint256", "name": ""}], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_repoURL"}], "constant": false, "name": "getNumberBounties", "outputs": [{"type": "uint256", "name": ""}], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_issueURL"}, {"type": "string", "name": "_claimee_metaData"}], "constant": false, "name": "claimBounty", "outputs": [], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_issueURL"}], "constant": false, "name": "clawbackExpiredBounty", "outputs": [], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_issueURL"}], "constant": false, "name": "rejectBountyClaim", "outputs": [], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_issueURL"}], "constant": false, "name": "bountydetails", "outputs": [{"type": "uint256", "name": ""}, {"type": "address", "name": ""}, {"type": "address", "name": ""}, {"type": "address", "name": ""}, {"type": "bool", "name": ""}, {"type": "bool", "name": ""}, {"type": "string", "name": ""}, {"type": "uint256", "name": ""}, {"type": "string", "name": ""}, {"type": "uint256", "name": ""}, {"type": "string", "name": ""}], "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": "index"}], "constant": false, "name": "_bountydetails", "outputs": [{"type": "uint256", "name": ""}, {"type": "address", "name": ""}, {"type": "address", "name": ""}, {"type": "address", "name": ""}, {"type": "bool", "name": ""}, {"type": "bool", "name": ""}, {"type": "string", "name": ""}, {"type": "uint256", "name": ""}, {"type": "string", "name": ""}, {"type": "uint256", "name": ""}, {"type": "string", "name": ""}], "payable": false, "type": "function"}, {"inputs": [{"type": "bytes32", "name": ""}], "constant": true, "name": "Bounties", "outputs": [{"type": "uint256", "name": "amount"}, {"type": "address", "name": "bountyOwner"}, {"type": "address", "name": "claimee"}, {"type": "string", "name": "claimee_metaData"}, {"type": "uint256", "name": "creationTime"}, {"type": "uint256", "name": "expirationTime"}, {"type": "bool", "name": "initialized"}, {"type": "string", "name": "issueURL"}, {"type": "string", "name": "metaData"}, {"type": "bool", "name": "open"}, {"type": "address", "name": "tokenAddress"}], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "_issueURL"}], "constant": false, "name": "approveBountyClaim", "outputs": [], "payable": false, "type": "function"}, {"inputs": [{"type": "string", "name": "str"}], "constant": false, "name": "strToMappingIndex", "outputs": [{"type": "bytes32", "name": "result"}], "payable": false, "type": "function"}, {"inputs": [{"indexed": false, "type": "address", "name": "_from"}, {"indexed": false, "type": "string", "name": "issueURL"}, {"indexed": false, "type": "uint256", "name": "amount"}], "type": "event", "name": "bountyPosted", "anonymous": false}, {"inputs": [{"indexed": false, "type": "address", "name": "_from"}, {"indexed": false, "type": "string", "name": "issueURL"}], "type": "event", "name": "bountyClaimed", "anonymous": false}, {"inputs": [{"indexed": false, "type": "address", "name": "_from"}, {"indexed": false, "type": "string", "name": "issueURL"}], "type": "event", "name": "bountyExpired", "anonymous": false}, {"inputs": [{"indexed": false, "type": "address", "name": "_from"}, {"indexed": false, "type": "address", "name": "payee"}, {"indexed": false, "type": "string", "name": "issueURL"}], "type": "event", "name": "bountyClaimApproved", "anonymous": false}, {"inputs": [{"indexed": false, "type": "address", "name": "_from"}, {"indexed": false, "type": "string", "name": "issueURL"}], "type": "event", "name": "bountyClaimRejected", "anonymous": false}]';
    bounty_abi = json.loads(abi_str);
    getBountyContract = web3.eth.contract(abi=bounty_abi, address=settings.BOUNTY_CONTRACT_ADDRESS);
    return getBountyContract