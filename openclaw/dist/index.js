"use strict";
// Copyright 2026 SupraWall Contributors
// SPDX-License-Identifier: Apache-2.0
Object.defineProperty(exports, "__esModule", { value: true });
exports.protect = void 0;
exports.secureClaw = secureClaw;
/**
 * suprawall Plugin for OpenClaw
 * Provides native interception for autonomous browser agents.
 */
const suprawall_1 = require("suprawall");
Object.defineProperty(exports, "protect", { enumerable: true, get: function () { return suprawall_1.protect; } });
/**
 * Secure an OpenClaw agent instance.
 *
 * Intercepts every browser command (click, type, navigate, etc.)
 * and audits it against your suprawall security policies.
 *
 * @example
 * import { secureClaw } from "@suprawall/claw";
 * const agent = new Clawbot(browser);
 * const secured = secureClaw(agent, { apiKey: "ag_..." });
 *
 * await secured.execute("Click 'Delete Account'"); // 🛡️ Intercepted
 */
function secureClaw(agent, options) {
    if (!agent.browser) {
        console.warn("🛡️ suprawall: Provided agent does not appear to be an OpenClaw instance (missing 'browser').");
    }
    // leverage the SDK's universal protect logic
    return (0, suprawall_1.protect)(agent, options);
}
