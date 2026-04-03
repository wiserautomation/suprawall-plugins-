/**
 * suprawall Plugin for OpenClaw
 * Provides native interception for autonomous browser agents.
 */
import { protect, SupraWallOptions } from "suprawall";
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
export declare function secureClaw(agent: any, options: SupraWallOptions): any;
export { protect as protect };
